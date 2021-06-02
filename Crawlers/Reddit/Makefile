run: 
	FILE=$$(python3 Reddit.py);\
	python3 DataCleaner.py $$FILE;
clean:
	rm CrawledData/*raw*.json