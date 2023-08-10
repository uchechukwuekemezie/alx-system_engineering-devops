#!/usr/bin/python3
"""
    counts number of words in hot posts of a given subreddit
"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """ counts the given words found in hot posts of a subreddit. """


    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "script for: 0x16.api.advanced: (by micoliser)"
            }
    params = {
        "after": after,
        "count": count,
        "limit": 100
        }
    res = requests.get(url,
            headers=headers,
            params=params,
            allow_redirects=False)

    if res.status_code == 404:
        return
    try:
        data = res.json().get("data")
    except Exception:
        return

    after = data.get("after")
    count += data.get("dist")
    for child in data.get("children"):
        title = child.get("data").get("title").lower()
        title_split = title.split()
        for word in word_list:
            l_word = word.lower()
            if l_word in title_split:
                times = len([tit for tit in title_split if tit == l_word])
                key = l_word
                try:
                    instances[key] += times
                except KeyError:
                    instances[key] = times

                    if after is None:
                        if len(instances) == 0:
                            print("")
                            return
                        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
                        [print("{}: {}".format(title, count)) for title, count in instances]
                        return

                    count_words(subreddit, word_list, instances, after, count)
                    
