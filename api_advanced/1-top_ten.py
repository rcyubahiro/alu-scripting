#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Fetch and print the titles of the first 10 hot posts for a subreddit."""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    HEADERS = {"User-Agent": "Python:top_ten_script:v1.0 (by /u/yourusername)"}

    try:
        response = requests.get(URL, headers=HEADERS, allow_redirects=False)
        if response.status_code == 200:
            hot_posts = response.json().get("data", {}).get("children", [])
            for post in hot_posts:
                print(post.get('data', {}).get('title'))
        else:
            print(f"Error: Received status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    finally:
        print("OK", end="\n")  # Print OK exactly once, no extra newlines


if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    top_ten(subreddit) 
