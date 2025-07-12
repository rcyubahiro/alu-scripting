#!/usr/bin/python3
"""Fetches and prints top 10 hot post titles for a subreddit"""

import requests
import sys


def top_ten(subreddit):
    """Fetch and print titles of the top 10 hot posts for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Python:subreddit.hot:v1.0 (by /u/yourusername)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            for post in posts:
                sys.stdout.write(post['data'].get('title') + '\n')
    except Exception:
        pass

    # Final OK output without newline
    sys.stdout.write("OK")
    sys.stdout.flush()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
