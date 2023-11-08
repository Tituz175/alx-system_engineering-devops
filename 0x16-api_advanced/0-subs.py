#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the numbes of subreddit subscriber
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"user-agent": "hshdl"}
    res = requests.get(url=url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    return res.json().get("data").get("subscribers")
