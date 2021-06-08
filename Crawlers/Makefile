run: 
	FILE=$$(python3 prepDirectory.py);\
	python3 Reddit/Crawler.py $$FILE; & python3 Newspapers/Crawler.py $$FILE\
	python3 Reddit/DataCleaner.py $$FILE & python3 Twitter/hashtagCrawler.py $$FILE & python3 Twitter/usertweetsCrawler.py $$FILE;\

newspapers: 
	FILE=$$(python3 prepDirectory.py);\
	python3 Newspapers/Crawler.py $$FILE

reddit:
	FILE=$$(python3 prepDirectory.py);\
	python3 Reddit/Crawler.py $$FILE;\
	python3 Reddit/DataCleaner.py $$FILE;

twitter: 
	FILE=$$(python3 prepDirectory.py);\
	python3 Twitter/hashtagCrawler.py $$FILE & python3 Twitter/usertweetsCrawler.py $$FILE;\
	
clean:
	rm CrawledData/