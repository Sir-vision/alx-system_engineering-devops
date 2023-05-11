#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:89.0)\
               Gecko/20100101 Firefox/89.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        for entry in data.get("children"):
            print(entry.get("data").get("title"))
    else:
        print("None")
        return
