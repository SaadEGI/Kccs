import json
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from newsplease import NewsPlease


def stemSentence(sentence):
    token_words = word_tokenize(sentence)
    stem_sentence = []
    stemmer = SnowballStemmer("english")

    for word in token_words:
        stem_sentence.append(stemmer.stem(word))
    return " ".join(stem_sentence)


def lemmSentence(sentence):
    lemma_sentence=[]
    lemmatizer = WordNetLemmatizer()

    for word in sentence:
        lemma_sentence.append(lemmatizer.lemmatize(word))
    return "".join(lemma_sentence)


# input_str = "\t \nThis &is [an] 2 33 example? {of} string. with.? 45 4 punctuation!!!!" # Sample string

# article = NewsPlease.from_url('https://www.nytimes.com/2021/06/19/world/americas/brazil-drought.html')
# # make a dictonary object from NewsPlease object
# d = article.__dict__

# # Convert it to string 
# s = json.dumps(d, indent=4, sort_keys=True, default=str)

# input_str = article.maintext

# # write it to json file
# with open('new.json', "w") as fp:
# 	fp.write(s)

with open('new.json') as json_file:
    data = json.load(json_file)
input_str = data["maintext"]


# Replace digits with space
input_str = re.sub(r"\d+", "", input_str)
# Remove punctuations, instead put spaces
result = input_str.translate(str.maketrans("", "", string.punctuation))
#cleaning up
result = re.sub(' +', ' ', result)
# remove whitespaces (tabs,..)
result = result.strip()

stop_words = set(stopwords.words('english'))

tokens = word_tokenize(result)
result = [i for i in tokens if not i in stop_words]

print (result)
result =  " ".join(result) 

print(stemSentence(result))
