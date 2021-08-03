import tweepy
import json
import sys
import csv
import socket


authentication = tweepy.OAuthHandler('ColqKqV1rfcpd1ytv9RMS37eO', 'otDk7hQGQebS1csNQ5K6aaEqRBHjatGNJmLWw4W31rumCK6ak7')
authentication.set_access_token('1014769894276128769-U4Vl2WwuqivDYqImj7TgZYentFMNfJ',
                                'lIXJ2do4p5W3sFmqokB2O8IYFr8o7kZjNh4l7IKxBK0kv')
api = tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def get_tweets(hashtag, listoflists):
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
            List = [hashtag, tweet.user.name, tweet.full_text, tweet.created_at, tweet.user.location,
                    tweet.favorite_count]
            listoflists.append(List)

        tweetCount += len(newTweets)
        maxId = newTweets[-1].id


## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
header = ['Hashtag', 'username', 'fulltext', 'Date', 'Location', 'Number of Likes', 'Number of Retweets']
listoflists = []
listoflists.append(header)
with open(r"Hashtags.txt") as f:
    lines = f.read().splitlines()
for li in lines:
    get_tweets(li, listoflists)

    with open("out.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(listoflists)

