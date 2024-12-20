import json
import pathlib
import requests
import argparse

######
# NOTE THAT:
# This program is not "battle tested" and if you do things that are not part of the
# "happy path" you may get errors with inscrutable messages. This example is about using 
# argparse, not about building a robust web querying tool.
# 
# Also note, reddit always returns a "pinned" post if there is one as well as the
# current top post, even if your limit value is set to 0.
######

def main():
    parser = argparse.ArgumentParser(
        description='Read the titles of the top n listings from a specified subreddit',
        epilog='\n==============\n'
    )

    parser.add_argument(
        "-r", "--subreddit", 
        help="The subreddit URL slug (excluding /r/). Defaults to the very wholesome /r/aww.", 
        type=str, 
        default="aww", 
    )

    parser.add_argument(
        "-n", "--num", 
        help="The number of posts to fetch from the front page. Default=1, allowed range=(1,25)", 
        type=int,
        default=1, 
        choices=range(1,26)
    )

    args = parser.parse_args()
    fetch_and_display_posts(args.subreddit, args.num)


def fetch_and_display_posts(subreddit, post_limit):
    
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}.json",
        params={
            'limit': post_limit
        },
        headers={
            'User-Agent': "Teb's Lab Programming Practice Bot"
        }
    )

    if response.status_code != 200:
        print("The response from reddit was not a success.")
        print(response.status_code)
        print(response.content)
        print("exiting program")
        exit(1)

    listing = response.json()

    # Extract the posts to loop over them
    posts = listing['data']['children']

    # Iterate over the posts, extract the data, print
    for post in posts:
        post_data = post['data']
        display_post(post_data)


def display_post(post_data):
    title = post_data['title']
    username = post_data['author']
    upvote_ratio = post_data['upvote_ratio']
    post_url = post_data['url']

    print(f'==== {title} ====')
    print(f'User: {username}\nUpvote Ratio: {upvote_ratio}\nURL: {post_url}')
    print()


if __name__ == '__main__':
    main()