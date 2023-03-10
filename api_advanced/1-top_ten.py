#!/usr/bin/python3
"""
returning the 10 posts
"""

import json
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json()['data']['choldren']
    for post in posts:
        print(post['data']['title'])

