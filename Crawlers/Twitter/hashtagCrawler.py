import tweepy
import json
import sys

authentication = tweepy.OAuthHandler('ColqKqV1rfcpd1ytv9RMS37eO', 'otDk7hQGQebS1csNQ5K6aaEqRBHjatGNJmLWw4W31rumCK6ak7')
authentication.set_access_token('1014769894276128769-U4Vl2WwuqivDYqImj7TgZYentFMNfJ',
                                    'lIXJ2do4p5W3sFmqokB2O8IYFr8o7kZjNh4l7IKxBK0kv')
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

