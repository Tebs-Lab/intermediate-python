import asyncio, aiohttp
import requests

# I wrote this helper function because it's much easier to
# write the code this way -- encapsulating the aysnc part of 
# handling each response individually into a function scope.
async def fetch_post_return_top_comment(url):
    async with aiohttp.ClientSession() as session:
        resp = await session.get(
            'https://www.reddit.com' + url + '.json', 
            headers={'User-Agent': 'cute-animal-pics-bot'}
        )
        json = await resp.json()
        comments = json[1]['data']['children']
        if len(comments) == 0:
            return 'No comments'
        return json[1]['data']['children'][0]['data']['body']


async def fetch_top_posts_with_top_comments_concurrent():
    # Synchronous, because this is just a script so we have to wait for this
    # to finish no matter what.
    all_listings_response = requests.get(
        'https://www.reddit.com/r/awww/top/.json?t=day&limit=5',
        headers={
            'User-Agent': 'cute-animal-pics-bot'
        }
    )

    # Extract today's top n posts
    top_n_post_urls = []
    for post in all_listings_response.json()['data']['children']:
        top_n_post_urls.append(post['data']['permalink'])

    # Fetch the comments for each post
    coroutines = []
    for url in top_n_post_urls:
        coroutines.append(asyncio.create_task(fetch_post_return_top_comment(url)))
    
    # Crucial note: the order of operation is not ensured but the order of the
    # return values IS the same as the input list, so we can zip like this safely
    top_comments = await asyncio.gather(*coroutines)
    for url, comment in zip(top_n_post_urls, top_comments):
        print(f'Top comment for {url}: {comment}')

asyncio.run(fetch_top_posts_with_top_comments_concurrent())