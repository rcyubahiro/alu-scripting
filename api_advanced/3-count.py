#!/usr/bin/python3
"""Recursive function to count keywords in hot posts titles of a subreddit"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Queries Reddit API recursively, counts occurrences of keywords in hot post titles,
    and prints sorted counts.

    Args:
        subreddit (str): Subreddit name.
        word_list (list): List of keywords to count (case-insensitive).
        after (str): Pagination token for Reddit API (used internally).
        counts (dict): Accumulated counts of keywords (used internally).

    Prints:
        Sorted counts of keywords in descending order by count, then alphabetically.
        Prints nothing if subreddit invalid or no matches.

    Returns:
        None
    """
    if counts is None:
        counts = {}

    # Normalize word_list to lowercase and sum duplicates
    word_list_lower = [w.lower() for w in word_list]
    word_set = set(word_list_lower)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "alu-api-project:v1.0 (by /u/yourusername)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 302 or response.status_code != 200:
            # Invalid subreddit or error
            if after is None:
                # Only print if first call and no data
                return
            else:
                # End recursion silently
                return

        data = response.json().get("data", {})
        children = data.get("children", [])

        for post in children:
            title = post.get("data", {}).get("title", "").lower().split()
            # Count occurrences of each keyword exactly (word boundaries)
            for word in word_set:
                # Count exact matches only (case-insensitive)
                # We consider words separated by spaces, punctuation breaks words
                # So we check exact matches in the split list
                count = title.count(word)
                if count > 0:
                    counts[word] = counts.get(word, 0) + count

        after = data.get("after")
        if after is None:
            # End recursion, print sorted results
            if counts:
                # Sort by count desc, then alphabetically asc
                sorted_counts = sorted(
                    counts.items(),
                    key=lambda x: (-x[1], x[0])
                )
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
            return

        return count_words(subreddit, word_list, after, counts)

    except requests.RequestException:
        # On request failure, print nothing
        return


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <subreddit> <list of keywords>")
        print(f"Ex: {sys.argv[0]} programming 'python java javascript'")
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])

