import json
import os
import time
from newsplease import NewsPlease
article = NewsPlease.from_url('https://en.wikipedia.org/wiki/Aleppo')

# make a dictonary object from NewsPlease object
d = article.__dict__

# Convert it to string 
s = json.dumps(d, indent=4, sort_keys=True, default=str)

# make file in same directory as this script; cite from sufyan :0
if(not os.path.exists('./CrawledData/')):
    os.mkdir('./CrawledData')

filename = f'{time.strftime("%Y%m%d-%H%M%S")}_raw.json'

# write it to json file
with open(f'./CrawledData/{filename}', "w") as fp:
	fp.write(s)
