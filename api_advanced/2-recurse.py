#!/usr/bin/python3
"""Recursive function to get all hot post titles for a subreddit"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries Reddit API to get all hot post titles for a subreddit.

    Args:
        subreddit (str): Subreddit name to query.
        hot_list (list): List of titles collected so far.
        after (str): The 'after' parameter for pagination.

    Returns:
        list: List of all hot post titles, or None if subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "alu-api-project:v1.0 (by /u/yourusername)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 302 or response.status_code != 200:
            return None

        data = response.json().get("data", {})
        children = data.get("children", [])

        for post in children:
            title = post.get("data", {}).get("title")
            if title:
                hot_list.append(title)

        after = data.get("after")
        if after is None:
            return hot_list

        return recurse(subreddit, hot_list, after)

    except requests.RequestException:
        return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        titles = recurse(sys.argv[1])
        if titles is None:
            print("None")
        else:
            print(len(titles))
