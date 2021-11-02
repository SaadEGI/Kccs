# Running the crawlers and cleaning the data

Simply run ```make run``` in your cli and all the crawlers (Reddit, Newspapers, twitter) will be run. At the end you should find a file from each crawler.

In case you go for this option, data crawled from all sources will be found in the same directory.

Optionaly, you cant specify which crawler you want to run. Currently you have the option to run ```make reddit```, ```make news``` or ```make twitter``` to run its respective crawler.

Finally, ```make clean``` deletes any and all crawled data. 

### Check Twitter Readme for  more informations

---


Note: any file containing the string ```Crawled``` **will not be pushed into the repository**, for it is specified in the .gitignore.
Reason for this is that the data is going to be too big for Github to accept it, aka it will be too big to be pushed to the remote repo.
