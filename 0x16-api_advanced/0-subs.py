#!/usr/bin/python3
"""Write a function that queries the Reddit API
    and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyApp/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        count = data.get('data').get('subscribers')
        return count
    return 0
