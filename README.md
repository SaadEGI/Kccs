#  Project title: When? How? and Where? – Detecting Diseases Outbreak through News
#### Incorporate the new advances from NLP to build a system able to help detect possible future outbreaks to support public policies.

## Motivation: 
 If one thing the COVID-19 outbreak showed us is that early actions can save many lives. However, decisions for such actions require updated information. While the first case of “unusual pneumonia” was first identified on the first minutes of 31/12/2019 (Bluedot), it was only on 25/02/2020 that the Director-General (World Health Organisation) Tedros Adhanom Ghebreyesus said the COVID-19 “absolutely” had the potential to become a pandemic, defined as the worldwide spread of a new disease. Now the question is not more “What if something like COVID-19 happens”, but instead “When? How? and Where?”. We want to incorporate the new advances from NLP (e.g., news analysis, (Multi)Language Models) to build a system to help detect possible future outbreaks to support public policies (decisions).

# Features
## Tech/framework used
#### Built with:

- Python
- Tweepy (API authentication needed)
- [Twint](https://github.com/twintproject) (API authentication NOT needed)
- [NewsFetch](https://github.com/santhoshse7en/news-fetch)

## Usage:

### Crawling

The project steps are still independent toeach other, that means, the crawling part will be done first using the Crawlers file and choosing one of these following source: 

1. ### Twitter

2. ### Newspapers
The list of newspaper websites provided in this repository is too big to be crawled at once without getting IP-banned, therefore the list was divided into a group of smaller lists that will be crawled individually. For each list, the crawler will get the latest (published in the last week) newsarticles and retrieve the following features:
    
1. Title
2. Website: which newspaper published this article?,
3. Description: a short summary of the article,
4. Main Text: the full article text
5. URL: for reference

After installing all dependencies: 

```bash
sudo pip3 install fake_useragent pandas random_user_agent newspaper3k beautifulsoup4;
sudo pip install news-please Unidecode;
```
,a list can be crawled using the following snippet: 

```bash 
python3  Crawlers/Newspapers/Crawler.py $(NumOfListToBeCrawled);
```

3. ### Reddit

Features gathered: 
1. Title
2. Full text
3. Permalink: relevant for reddits posts in which a link (e.g. article, video) is attached to the post
4. URL: for reference 
5. Comments (to a depth of 1, no nested comments collected) and URL's of each comment
After installing all dependencies: 

```bash
sudo pip3 install fake_useragent numpy requests newspaper3k news-please beautifulsoup4 Unidecode pandas;
```

, the following snippet can be used to crawl Reddit 

```python
cd Crawlers/;
FILE=$(python3 prepDirectory.py); # Creates a directory for the outputs of Crawler.py and DataCleaner.py
python3 Reddit/Crawler.py $FILE; # Crawls latest posts from the proided list of subreddits
python3 Reddit/DataCleaner.py $FILE; # Cleans the crawled data of any unneeded features
```


### Analysis:

For the analysis part, there is an Exploratory data analysis that need to be extended, until now this analysis is done on Twitter/newsheadlines Datasets



# Results