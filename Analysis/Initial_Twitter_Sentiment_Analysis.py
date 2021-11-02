import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import nltk
import re
import string
import csv
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from textblob import TextBlob
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer


def percentage(part,whole):
	return 100 * float(part)/float(whole)



def cleaning(sentence):
	sentence = sentence.lower()
	sentence = re.sub(r"\d+", "", sentence)
	result = sentence.translate(str.maketrans("", "", string.punctuation))
	result = ''.join([i if ord(i) < 128 else ' ' for i in result])
	result = re.sub(' +', ' ', result)
	# re.sub(r'[^\x00-\x7f]',r'', result)
	# result = result.strip()
	# stop_words = set(stopwords.words('english'))
	# result = [i for i in result if not i in stop_words]
	# tokens = word_tokenize(result)
	# result = [i for i in tokens if not i in stop_words]
	# result =  " ".join(result)
	return result


with open('30k_tweets_Dataset.csv', newline='', encoding="utf8") as f:
    reader = csv.reader(f)
    my = list(reader)


neu  = []
for tweet in my:
	tweet = cleaning(''.join(tweet))
	neu.append(tweet)

tweets  = [x for x in neu if x] # remove some empty elements

neu2 = []
positive = 0
negative = 0
neutral = 0
polarity = 0
tweet_list = []
neutral_list = []
negative_list = []
positive_list = []

for tweet in tweets:
	tweet_list.append(tweet)
	analysis = TextBlob(tweet)
	score = SentimentIntensityAnalyzer().polarity_scores(tweet)
	print(score)
	neg = score['neg']
	neu = score['neu']
	pos = score['pos']
	comp = score['compound']
	polarity += analysis.sentiment.polarity
	if neg > pos:
		negative_list.append(tweet)
		negative = negative + 1
	elif pos > neg:
		positive_list.append(tweet)
		positive = positive + 1
	elif pos == neg:
		neutral_list.append(tweet)
		neutral = neutral + 1
	positive = percentage(positive, 61)
	negative = percentage(negative, 61)
	neutral = percentage(neutral, 61)
	polarity = percentage(polarity, 61)
	positive = format(positive, '.1f')
	negative = format(negative, '.1f')
	neutral = format(neutral, '.1f')

	# if score['neg'] and score['neu'] and score['pos'] and score['compound']:
	# 	neu2.append(tweet)


tweet_list = pd.DataFrame(tweet_list)
neutral_list = pd.DataFrame(neutral_list)
negative_list = pd.DataFrame(negative_list)
positive_list = pd.DataFrame(positive_list)
print("total number: ",len(tweet_list))
print("positive number: ",len(positive_list))
print("negative number: ",len(negative_list))
print("neutral number: ",len(neutral_list))