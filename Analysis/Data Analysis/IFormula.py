def calculatetf(wordDict, bag):
	tfDict ={}
	bagcount = len(bag)
	for word,count in wordDict.items():
		tfDict[word] = count / float(bagcount)
	return tfDict
