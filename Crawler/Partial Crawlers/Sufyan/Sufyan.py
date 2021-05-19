# This crawler is made to crawl a list of subreddits available @ giveSomeUrl
import urllib.request
import urllib.parse

BASEURL='https://www.reddit.com/r/'



SubredditsList = []
with open('SubredditList') as f:
    for line in f:
        SubredditsList.append(BASEURL+line.strip())





# https://www.git .com/dev/api/#GET_{sort}
# + https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example
#1. Get a list of all posts of the last month throught the two above pages

# 2. crawl the posts individually by appending the .json to its end. this will return two objects, the first one at index 0 
# includes the post, the second object at index 1 includes the comments


# 3. save posts in a folder called scraped data or smth in json format
# 3.1 maybe use pandas and dataframes for dealing with the data 