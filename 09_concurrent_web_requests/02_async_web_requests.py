# Although there are many uses for concurrency and async,
# the most common example for Python developers is making 
# web requests. aiohttp is a popular library for making
# requests using asyncio.

# Install the two libraries we need.
'''
pip install aiohttp aiodns
or
pip install aiohttp[speedups]
'''
import aiohttp
import asyncio

# aiohttp is built around the concept of a "session" which makes it
# slightly harder to use compared to requests. They discuss this decision
# in their design here: https://docs.aiohttp.org/en/stable/http_request_lifecycle.html
async def download_url(url):
    print(f'Downloading {url}')
    # This max field size is because Twitter sends at least one header that is larger than the default 
    # maximum value.
    async with aiohttp.ClientSession(max_field_size=8190 * 2) as session:
        resp = await session.get(url) # The actual web request is made.
        text = await resp.text() # long responses may be read into a text buffer not RAM, so async again.
        print(f'Downloaded {url}, size {len(text)}')


async def run():
    await asyncio.gather(
        download_url('https://www.facebook.com'),
        download_url('https://www.twitter.com'),
        download_url('https://www.stackoverflow.com'),
        download_url('https://www.google.com')
    )

# Kick things off...
asyncio.run(run())
print("WE DID IT!!!!")