import sys
import os
import time


if(not os.path.exists('./CrawledData/')):
    os.mkdir('./CrawledData')

filename = f'{time.strftime("%Y-%m-%d_%H:%M:%S")}'
os.mkdir(f'./CrawledData/{filename}')
os.chdir(f'{os.getcwd()}/CrawledData')

print(f'{os.getcwd()}/{filename}')
sys.exit(0)
