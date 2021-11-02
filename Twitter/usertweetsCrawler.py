import sys
import tweepy
import datetime, time
import json

##Private, please do not share these codes with anyone, thanks
authentication = tweepy.OAuthHandler('XXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXX')
authentication.set_access_token('XXXXXXXXXXXXXXX-XXXXXXXXXXXXXXX',
                                    'XXXXXXXXXXXXXXX')

api = tweepy.API(authentication)

file_path = sys.argv[1]

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
with open(r"ListofKeywords") as f:
    lines = f.read().splitlines()
for li in lines:
    usertweets[get_tweets(api, li)] = None

with open('usertweets.json', 'w', encoding='utf-8') as f:
    json.dump(usertweets, f, ensure_ascii=False, indent=4)


