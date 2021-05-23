import json
import sys

data = {}
cleanedData = {}

files = sys.argv[1:]

for file in files:
    with open(f'./CrawledData/{file}') as f:
        data = json.load(f)
        for subreddit in data:
            cleanedData[subreddit] = {}
            index = 0
            for child in data[subreddit]:
                temp = []
                cleanedData[subreddit][str(index)] = {}
                cleanedData[subreddit][str(index)] = {
                    'thread': {
                    'title': data[subreddit][child][0]['data']['children'][0]['data']['title'],
                    'selftext': data[subreddit][child][0]['data']['children'][0]['data']['selftext'],
                    'permalink': data[subreddit][child][0]['data']['children'][0]['data']['permalink'],
                    'url': data[subreddit][child][0]['data']['children'][0]['data']['url'],
                    },
                'comments': data[subreddit][child][1]['data']['children']
                }

                for comment in cleanedData[subreddit][str(index)]['comments']:
                    comment = {
                        'body':  comment['data'].get('body'),
                        'permalink': comment['data'].get('permalink'),
                    }
                    temp.append(comment)
                cleanedData[subreddit][str(index)]['comments'] = temp
                index = index + 1


with open('./CrawledData/'+f'{file[:-8]}'+'cleaned'+'.json', "w") as fp:
    json.dump(cleanedData, fp, indent = 4)



                
