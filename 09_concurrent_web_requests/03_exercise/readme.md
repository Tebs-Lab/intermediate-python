# Async Exercise

Take a solution (yours or ours) from last week's class and refactor it to use aiohttp. You should be able to substantially speed up the script by:

* Fetching each individual post concurrently.
* Fetching each individual comment on each post concurrently.

This exercise is easy to describe, and harder to implement. Good luck and here are some useful resources:

* [aiohttp documentation](https://docs.aiohttp.org)
* [RealPython's async tutorial](https://realpython.com/async-io-python/)
    * With some aiohttp specific examples.

## A Few Hints:

* Use the 'limit' query parameter on the posts request to avoid getting rate limited by Reddit.
    * (your instructor learned this the hard way...)
* Make life easier by using function scope to eliminate any shared resources.
* One step at a time -- figure out how to make the initial requests to fetch each post async first.
    * While leaving the handling of each one synchronous with `requests`
    * THEN once that works, handle the comments with async.