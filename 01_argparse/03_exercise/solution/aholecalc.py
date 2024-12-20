import requests
import pathlib
import argparse

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

def main():
    parser = argparse.ArgumentParser(
        description='Calculate today\'s top aholes from Reddit.',
        epilog='\n==============\n'
    )

    parser.add_argument(
        "-o", "--output", 
        help="The name of the directory to store today's judgements. If left blank nothing will be saved.", 
        type=str 
    )

    parser.add_argument(
        "-p", "--posts", 
        help="The number of posts to fetch from the homepage.", 
        type=int, 
        default=25, 
    )

    parser.add_argument(
        "-c", "--comments", 
        help="The number of comments to fetch from each post. Default=25", 
        type=int,
        default=25,
    )

    parser.add_argument(
        "--nta", 
        help="The threshold for the ratio of NTA votes to selected comments to be included in the summary.", 
        type=float,
        default=0.0,
        choices=FloatRange(0.0, 1.0)
    )

    parser.add_argument(
        "--yta", 
        help="The threshold for the ratio of YTA votes to selected comments to be included in the summary.", 
        type=float,
        default=0.0,
        choices=FloatRange(0.0, 1.0)
    )

    parser.add_argument(
        "--esh", 
        help="The threshold for the ratio of ESH votes to selected comments to be included in the summary.", 
        type=float,
        default=0.0,
        choices=FloatRange(0.0, 1.0)
    )

    parser.add_argument(
        "--nah", 
        help="The threshold for the ratio of NAH votes to selected comments to be included in the summary.", 
        type=float,
        default=0.0,
        choices=FloatRange(0.0, 1.0)
    )

    args = parser.parse_args()

    # Handle the output flag initial setup
    if args.output:
        output_dir = pathlib.Path(__file__).parent / args.output
        output_dir.mkdir(exist_ok=True)

        # to avoid polluting the github, we add output folders to the gitignore file.
        with open(pathlib.Path(__file__).parent / '.gitignore', 'r+') as f:
            path_to_ignore = args.output + '/'
            lines = []
            while (line := f.readline()) != '': lines.append(line)
                
            if path_to_ignore not in lines:
                f.write('\n' + path_to_ignore)

    # Fetch the requested number of posts
    top_urls = fetch_top_urls(n_posts = args.posts)

    print(f'======Top Daily AHole Judgements====')
    for url in top_urls:
        votes = compute_votes_from_post_url(url, args.comments)
        
        # Filter based on the optional ratios.
        # this filtering is an AND based mechanism -- e.g. if the user
        # specifies multiple thresholds then a post must meet all of them
        # to be included.
        include = True
        total_votes_cast = votes['YTA'] + votes['NTA'] + votes['ESH'] + votes['NAH']
        filter_map = [('YTA', args.yta), ('NTA', args.nta), ('ESH', args.esh), ('NAH', args.nah)]
        for vote_type, ratio_threshold in filter_map:
            if ratio_threshold != None:
                ratio = votes[vote_type] / total_votes_cast
                include = include and ratio >= ratio_threshold

        if include:
            summary_text = AHOLE_FORMAT_STRING.format(url=url, **votes)
            print(summary_text)

        # Write the output if requested
        if args.output:
            post_mini_title = url.split('/')[-2]
            with open(output_dir / f'{post_mini_title}', 'w') as outfile:
                outfile.write(summary_text)


def fetch_top_urls(n_posts=-1):
    # Get the top posts from today.
    all_listings_response = requests.get(
        'https://www.reddit.com/r/AmItheAsshole/top/.json?t=day',
        headers={
            'User-Agent': 'top-daily-ahole-calculator-bot'
        }
    )

    # Extract today's top n posts (set to 3 here to reduce rate limiting):
    top_n_post_urls = []
    for post in all_listings_response.json()['data']['children'][:n_posts]:
        top_n_post_urls.append(post['data']['url'])

    return top_n_post_urls


def compute_votes_from_post_url(url, comment_limit=-1):
    # fetch the comments
    comment_response = requests.get(
        url + '.json',
        headers={
            'User-Agent': 'top-daily-ahole-calculator-bot'
        },
        params = {
            'limit': comment_limit
        }
    )

    comments_json = comment_response.json()

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


# This funky looking class allows us to use the choices=FloatRange(0.0, 1.0) in
# arg parse. This also foreshadows much of what we are working on in future sessions
# on classes and objects.
class FloatRange(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __contains__(self, other):
        return self.start <= other <= self.end

    def __getitem__(self, index):
        if index == 0: return self
        raise IndexError()
    
    def __len__(self):
        return 1
    
    def __str__(self):
        return f'Bound float ({self.start, self.end})'

if __name__ == '__main__':
    main()