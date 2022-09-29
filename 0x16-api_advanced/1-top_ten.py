#!/usr/bin/python3
"""Returns the number of subscribers for a given subreddit.
If an invalid subreddit is given, the function should return 0."""
import json
import requests


def top_ten(subreddit):
    """
    It takes a subreddit as an argument,
    and returns the number of subscribers that subreddit has

    :param subreddit: the subreddit to query
    :return The number of subscribers of a subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'User-Agent': 'Custom Agent', 'From': 'eidengabriel07@gmail.com'}
    param = {"limit": 10}
    request = requests.get(url, params=param, headers=header)

    if request.status_code == 404:
        return 0
    results = request.json().get("data")
    for c in results.get("children"):
        print(c.get("data").get("title"))
