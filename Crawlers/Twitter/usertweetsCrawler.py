import sys
import tweepy
import datetime, time
import json

##Private, please do not share these codes with anyone, thanks
authentication = tweepy.OAuthHandler('ColqKqV1rfcpd1ytv9RMS37eO', 'otDk7hQGQebS1csNQ5K6aaEqRBHjatGNJmLWw4W31rumCK6ak7')
authentication.set_access_token('1014769894276128769-U4Vl2WwuqivDYqImj7TgZYentFMNfJ',
                                    'lIXJ2do4p5W3sFmqokB2O8IYFr8o7kZjNh4l7IKxBK0kv')

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
with open(r"Twitterlist") as f:
    lines = f.read().splitlines()
for li in lines:
    usertweets[get_tweets(api, li)] = None

with open('usertweets.json', 'w', encoding='utf-8') as f:
    json.dump(usertweets, f, ensure_ascii=False, indent=4)


