
# Mini-exercise: rewrite this code such that the downloading of all the individual posts
# is done concurrently. (Theres no reason to make the first one async in this scripting
# type workflow, but you could if you want -- in an application with other things going
#  it would help, but in this scripting workflow it's not necessary.)

# HINT!! Write a second function to encapsulate handling a single request-response
# lifecycle that returns the top comment data...

import requests
def fetch_top_posts_with_top_comments():
    all_listings_response = requests.get(
        'https://www.reddit.com/r/awww/top/.json?t=day&limit=5', # Using limit 5 to avoid rate limits!
        headers={
            'User-Agent': 'cute-animal-pics-bot'
        }
    )

    # Extract today's top n posts
    top_n_post_urls = []
    for post in all_listings_response.json()['data']['children']:
        top_n_post_urls.append(post['data']['permalink'])

    # Fetch the comments for each post
    for url in top_n_post_urls:
        r = requests.get(
            'https://www.reddit.com' + url + '.json', 
            headers={'User-Agent': 'cute-animal-pics-bot'}
        )
        json = r.json()
        comments = json[1]['data']['children']
        if len(comments) == 0:
            print('No comments')
        else:
            print(f'Top comment for {url}: {comments[0]["data"]["body"]}')

fetch_top_posts_with_top_comments()