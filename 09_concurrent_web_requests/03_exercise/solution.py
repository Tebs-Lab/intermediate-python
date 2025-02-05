import requests
import pathlib
import asyncio, aiohttp

# Reusable format string for printing
AHOLE_FORMAT_STRING = """
URL: {url}
==========================
The Situation: {situation}
==========================

Votes:
YTA: {YTA}
NTA: {NTA}
ESH: {ESH}
NAH: {NAH}
"""

async def main():
    top_urls = await fetch_top_urls()

    # Bonus, create a folder to store the summary judgments:
    output_dir = pathlib.Path(__file__).parent / 'judgments'
    output_dir.mkdir(exist_ok=True)
    
    coroutines = []
    for url in top_urls:
        coroutines.append(asyncio.create_task(compute_votes_from_post_url(url)))

    # We *could* get potentialy speed increases by not gathering here, and instead 
    # moving the printing into the async portion of the workload. But we'd also
    # risk things being out of order, and making the code harder to follow.
    all_votes = await asyncio.gather(*coroutines)

    print(f'======Top Daily AHole Judgements====')
    for url, votes in zip(top_urls, all_votes): 
        summary_text = AHOLE_FORMAT_STRING.format(url=url, **votes)
        print(summary_text)

        # Bonus: write each post to it's own file!
        post_mini_title = url.split('/')[-2]

        with open(output_dir / f'{post_mini_title}', 'w') as outfile:
            outfile.write(summary_text)

# I made this async for demonstration purposes, but because of the way it's
# awaited in main with no other coroutines to speak of, it doesn't really help.
async def fetch_top_urls(n_posts=-1):
    # Get the top posts from today.
     async with aiohttp.ClientSession() as session:
        all_listings_response = await session.get( 
            'https://www.reddit.com/r/AmItheAsshole/top/.json?t=day&limit=5',  # Using limit 5 to avoid rate limits!
            headers={'User-Agent': 'top-daily-ahole-calculator-bot'}
        )
        all_listing_data = await all_listings_response.json()
    
        # Extract today's top n posts (set to 3 here to reduce rate limiting):
        top_n_post_urls = []
        for post in all_listing_data['data']['children'][:n_posts]:
            top_n_post_urls.append(post['data']['url'])

        return top_n_post_urls


async def compute_votes_from_post_url(url):
    # fetch the comments
    async with aiohttp.ClientSession() as session:
        resp = await session.get(
            url + '.json', 
            headers={'User-Agent': 'ahole-judgement-bot'}
        )
        comments_json = await resp.json()

    votes = {
        'YTA': 0,
        'NTA': 0,
        'ESH': 0,
        'NAH': 0
    }

    # The comments listing is always the second item in the post.
    comments = comments_json[1]['data']['children']
    for comment in comments:
        if comment['kind'] != 't1': continue # t1 is the comment type, sometimes other types appear like "more"
        text = comment['data']['body']
        
        for vote_type in votes.keys():
            if vote_type in text:
                votes[vote_type] += 1

     # Some API's have deeply nested (and weird) data patterns, look at this monstrosity:
    votes['situation'] =  comments_json[0]['data']['children'][0]['data']['selftext']
    return votes

if __name__ == '__main__':
    asyncio.run(main())