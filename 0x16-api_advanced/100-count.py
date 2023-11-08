#!/usr/bin/python3
"""
Write a function that queries the Reddit API
and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def count_words(subreddit, word_list, after=None, word_dict={}):
    """
    Prints the titles of the first 10 hot
    posts listed for a given subreddit.
    """
    word_set = set([word.lower() for word in word_list])
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "shdh"}

    params = {
        "after": after,
    }
    res = requests.get(url=url, headers=headers,
                       allow_redirects=False, params=params)

    if res.status_code != 200:
        return None

    post_list = res.json().get("data").get("children")
    for post in post_list:
        word_titles = post.get("data").get("title").lower().split()
        for word in word_set:
            word_dict[word] = word_dict.get(word, 0) + word_titles.count(word)

    after = res.json().get("data").get("after")

    if after:
        count_words(subreddit, word_list, after, word_dict)
    else:
        word_list.sort(key=lambda x: word_dict.get(x), reverse=True)
        for word in word_list:
            if word_dict.get(word):
                print("{}: {}".format(word, word_dict.get(word)))
