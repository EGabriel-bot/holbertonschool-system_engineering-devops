#!/usr/bin/python3
"""Returns the number of subscribers for a given subreddit.
If an invalid subreddit is given, the function should return 0."""
import requests
import json


def number_of_subscribers(subreddit):
    """
    It takes a subreddit as an argument,
    and returns the number of subscribers that subreddit has

    :param subreddit: the subreddit to query
    :return: The number of subscribers of a subreddit.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'Custom Agent', 'From': 'eidengabriel07@gmail.com'}
    request = requests.get(url, headers=header)
    request_json = json.loads(request.text)

    if request.status_code == 404:
        return 0
    else:
        return request_json['data']['subscribers']
