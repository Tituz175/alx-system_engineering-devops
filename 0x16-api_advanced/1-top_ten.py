#!/usr/bin/python3
"""
Write a function that queries the Reddit API
and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot
    posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "hshdl"}
    params = {
        "limit": 10
    }
    res = requests.get(url=url, headers=headers,
                       allow_redirects=False, params=params)
    if res.status_code != 200:
        print(None)
        return 0
    post_list = res.json().get("data").get("children")
    for post in post_list:
        print(post.get("data").get("title"))
