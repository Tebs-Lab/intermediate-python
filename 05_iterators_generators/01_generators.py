import pathlib
import requests
# Generators are functions that can lazily generate a series of values.
# These are most useful when you are iterating over something that would
# be too large to fit in memory, or that requires an expensive operation
# to compute -- so you want to do it "just in time".

# Here's a simple example to show the syntax and use of a generator:
def simple_generator():
    yield 1
    yield 2
    yield 3

# To use a generator you can either call the "next" object on it...
x = simple_generator()
print(next(x))
print(next(x))
print(next(x))

# Once the operation is out of yields, it will raise a StopIteration exception.
# print(next(x)) # exception.

# For loops are designed to automatically catch StopIteration exceptions:
for i in simple_generator():
    print(i)

# Lets see a practical example.
# This generator reads the complete work of Shakespeare from a file, and yields
# one line at a time. This stops you from having to load the entire text into 
# memory. Such workloads are especially common in "big data" processing.
def shakespeare_generator():
    shakespear_path = pathlib.Path(__file__).parent / 'assets/shakespear.txt'
    with open(shakespear_path, 'r') as f:
        for line in f:
            yield line

# We can print things one line at a time
# or of course we could do more processing as well.
for line in shakespeare_generator():
    print(line)


# Another practical example is requesting pages of data from a web API.
# In this example we query Reddit's "popular" page to get the first 20
# posts, then if we reach the end of the results, we request the next page:
def fetch_popular_reddit(page_limit=3):
    current_page = 1
    url = 'https://www.reddit.com/r/popular.json'
    after = None

    # We'll stop after a preset page limit 
    while current_page <= page_limit:
        params = {'limit': 20}
        if after:
            params['after'] = after
        
        response = requests.get(url, params=params, headers={'User-agent': 'Pagination Example Bot'})
        response.raise_for_status() # just incase we get rate limited or something

        data = response.json()
        for post in data['data']['children']:
            yield post['data']
        after = data['data']['after']
        
        # If there are no more pages from reddit, we stop.
        if after is None:
            return
        
        # Finally, advance the page counter
        current_page += 1


reddit_request_generator = fetch_popular_reddit()
for post in reddit_request_generator:
    print(post['title'])
    print(post['url'])
    print()

# Micro-exercise: write a generator the yields the first N numbers of
# the Fibonacci sequence, where N is a parameter to the generator.