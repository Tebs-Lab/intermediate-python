# Sometimes we want to test some behavior that normally relies on 
# some external system, but we don't want to actually rely on that 
# system for our tests. 

# For example, supposed we want to test a flow that involves recovering from
# a network or server error, but we don't actually want to cause the network
# or external server to fail. For this, we can use the unittest.mock module.

# Note: the following are written for the pytest runner, but you can use unittest.mock
# with standard unittests as well.
import pytest
import unittest.mock as mock
from requests.exceptions import HTTPError

# We're going to mock the requests library so that we can simulate a network error.
requests = mock.Mock()

# This function NORMALLY uses the requests library to get the top posts from
# an internet forum dedicated to pictures of cute animals (www.reddit.com/r/awww)
# but we don't want to actually make requests to the internet in our tests. So 
# instead, we're going to "mock" the requests library to "pretend" to call the 
# network and force a particular result.
# Note, for simplicity we're just defining the function to be tested right here. 
def fetch_top_urls():
    # Get the top posts from today.
    all_listings_response = requests.get(
        'https://www.reddit.com/r/awww/top/.json?t=day',
        headers={
            'User-Agent': 'top-daily-ahole-calculator-bot'
        }
    )
    all_listings_response.raise_for_status()

    top_n_post_urls = []
    for post in all_listings_response.json()['data']['children']:
        top_n_post_urls.append(post['data']['url'])

    return top_n_post_urls

# This function returns a mock object that simulates a network request.
# it is limited compared to a full requests.Response object, but has 
# enough to test the function above (and more)
# From: https://gist.github.com/evansde77/45467f5a7af84d2a2d34f3fcb357449c
def _mock_response(
        status=200,
        content="CONTENT",
        json_data=None,
        raise_for_status=None):
    
    mock_resp = mock.Mock()
    # mock raise_for_status call w/optional error
    mock_resp.raise_for_status = mock.Mock()
    if raise_for_status:
        mock_resp.raise_for_status.side_effect = raise_for_status
    # set status code and content
    mock_resp.status_code = status
    mock_resp.content = content
    # add json data if provided
    if json_data:
        mock_resp.json = mock.Mock(
            return_value=json_data
        )
    return mock_resp

def test_network_error():
    # This context manager will catch any HTTPError exceptions that are raised
    # and report a failing test if one is NOT raised.
    with pytest.raises(HTTPError) as e:
        # First, we make a mock response representing an error.
        mock_resp = _mock_response(status=500, raise_for_status=HTTPError("Reddit is down."))
        
        # Then we tell the mock requests.get to return that response when called
        requests.get.return_value = mock_resp
        
        # Now when we call this function, when it calls requests.get, it will
        # result in a 500 error, which will raise an HTTPError.
        fetch_top_urls()

# We could also test a successful network request.
def test_network_success():
    mock_resp = _mock_response(status=200, json_data={
        'data': {
            'children': [
                {'data': {'url': 'https://www.reddit.com/r/awww/1'}},
                {'data': {'url': 'https://www.reddit.com/r/awww/2'}},
                {'data': {'url': 'https://www.reddit.com/r/awww/3'}}
            ]
        }
    })
    
    # Then we tell the mock requests.get to return that response when called
    requests.get.return_value = mock_resp
    
    # Now when we call this function, when it calls requests.get we'll have
    # a mock object whose .json() method returns the data above. If that were
    # the data from reddit, we'd know our code SHOULD return the following list.
    r = fetch_top_urls()
    assert mock_resp.raise_for_status.called
    assert r == [
        'https://www.reddit.com/r/awww/1',
        'https://www.reddit.com/r/awww/2', 
        'https://www.reddit.com/r/awww/3'
    ]


if __name__ == '__main__':
    pytest.main([__file__]) # only runs this file's tests