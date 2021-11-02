import tweepy
import json
import sys

authentication = tweepy.OAuthHandler('XXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXX')
authentication.set_access_token('XXXXXXXXXXXXXXX-XXXXXXXXXXXXXXX',
                                    'XXXXXXXXXXXXXXX')
api = tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def get_tweets(hashtag, usertweets):

    tweetsPerQry = 100

    maxTweets = 100

    maxId = -1
    tweetCount = 0

    while tweetCount < maxTweets:
        if (maxId <= 0):
            newTweets = api.search(q=hashtag, count=tweetsPerQry, result_type="recent", tweet_mode="extended")
        else:
            newTweets = api.search(q=hashtag, count=tweetsPerQry, max_id=str(maxId - 1), result_type="recent",
                                   tweet_mode="extended")

        if not newTweets:
            print("End")
            break

        for tweet in newTweets:
            usertweets[tweet.full_text] = None

        tweetCount += len(newTweets)
        maxId = newTweets[-1].id


usertweets = {}
file_path = sys.argv[1]
with open(r"Hashtags.txt") as f:
    lines = f.read().splitlines()
for li in lines:
    usertweets[get_tweets(li, usertweets)] = None

with open(rf'{file_path+"/twitterhashtagstweets.json"}', 'w', encoding='utf-8') as f:
        json.dump(usertweets, f, ensure_ascii=False, indent=4)

