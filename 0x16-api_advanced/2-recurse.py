#!/usr/bin/python3
"""
Write a function that queries the Reddit API
and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    Prints the titles of the first 10 hot
    posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "hshdl"}

    params = {
        "limit": 100,
        "after": after,
        "count": count
    }
    res = requests.get(url=url, headers=headers,
                       allow_redirects=False, params=params)
    if res.status_code != 200:
        return None

    post_list = res.json().get("data").get("children")
    for post in post_list:
        hot_list.append(post.get("data").get("title"))

    after = res.json().get("data").get("after")
    count += res.json().get("data").get("dist")

    if after:
        recurse(subreddit, hot_list, after, count)
    return hot_list
