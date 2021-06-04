import tweepy
import json

tweetsPerQry = 100
# test
maxTweets = 100
hashtag = "#corona"  # test
usertweets = {}
a = 0
##Private, please do not share these codes with anyone, thanks
authentication = tweepy.OAuthHandler('9Fmf0uyQ4kAlgfqLTRCgmvAXS', 'ASKvsmRRf4sVfv06y12H2VMKT4m3iarQUDuRnbcSRIDiVIg5Ha')
authentication.set_access_token('2993256339-ptMVZ0jCyGZWJfE9u7hnulkG1s0OlmbT1wMJ06l',
                                'x5p9NYlH6B7QNXWiB2OB4DyqmqW3gQePrjUWoIzxIet4q')
api = tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
maxId = -1
tweetCount = 0
# possibilty to add hashtags list here
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

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(usertweets, f, ensure_ascii=False, indent=4)



