import sys
import tweepy
import datetime, time
import json

authentication = tweepy.OAuthHandler('9Fmf0uyQ4kAlgfqLTRCgmvAXS', 'ASKvsmRRf4sVfv06y12H2VMKT4m3iarQUDuRnbcSRIDiVIg5Ha')
authentication.set_access_token('2993256339-ptMVZ0jCyGZWJfE9u7hnulkG1s0OlmbT1wMJ06l',
                                'x5p9NYlH6B7QNXWiB2OB4DyqmqW3gQePrjUWoIzxIet4q')
api = tweepy.API(authentication)


def get_tweets(api, username):
    page = 1
    deadend = False
    while True:
        tweets = api.user_timeline(username, page=page)

        for tweet in tweets:
            if (datetime.datetime.now() - tweet.created_at).days < 14:
                # Do processing here
                print(tweet.text.encode("utf-8"))
            else:
                deadend = True
                return
        if not deadend:
            page + 1
            time.sleep(500)


usertweets = {}
with open(r"twitterlist.txt") as f:
    lines = f.read().splitlines()
for li in lines:
    usertweets[get_tweets(api, li)] = None

with open('mydata.json', 'w') as file:
    json.dump(usertweets, file)


