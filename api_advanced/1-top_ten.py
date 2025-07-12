#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints titles of the first 10 hot posts.

    If subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Python:1-top_ten_script:v1.0 (by /u/yourusername)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if subreddit exists: status code 200 and no redirect
        if response.status_code == 200:
            data = response.json().get("data", {})
            children = data.get("children", [])
            if not children:
                print(None)
                return
            for post in children:
                title = post.get("data", {}).get("title")
                if title:
                    print(title)
        else:
            # If status code is 302 or other, subreddit likely invalid
            print(None)
    except requests.RequestException:
        print(None)
