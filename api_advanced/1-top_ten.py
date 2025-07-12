#!/usr/bin/python3
"""Exports top 10 hot post titles for a subreddit using Reddit API"""

import requests
import sys


def top_ten(subreddit):
    """Fetches and prints the titles of the top 10 hot posts for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Python:subreddit.hot:v1.0 (by /u/yourusername)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            for post in posts:
                title = post['data'].get('title')
                if title is not None:
                    print(title)
    except Exception:
        pass

    print("OK", end="", flush=True)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <subreddit>".format(sys.argv[0]))
        sys.exit(1)
    top_ten(sys.argv[1])
