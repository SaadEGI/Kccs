import json
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from newsplease import NewsPlease
from sklearn.feature_extraction.text import CountVectorizer

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

def normatizeDocument(sentence):
    sentence = re.sub(r"\d+", "", sentence)
    # Remove punctuations, instead put spaces
    result = sentence.translate(str.maketrans("", "", string.punctuation))
    #cleaning up
    result = re.sub(' +', ' ', result)
    # remove whitespaces (tabs,..)
    result = result.strip()


    stop_words = set(stopwords.words('english'))

    tokens = word_tokenize(result)
    result = [i for i in tokens if not i in stop_words]

    result =  " ".join(result)
    return result

def createWordVector(articles): # takes a list containing all articles to be vectorized as an argument
    # Technique is called count vectorization
    vectorizer = CountVectorizer()
    wordVectors = vectorizer.fit_transform(articles)
    return wordVectors.toarray()


document = "\t \nThis &is [an] 2 33 example? {of} string. with.? 45 4 punctuation!!!!" # Sample string

print(document)
result = stemSentence(normatizeDocument(document))
print(result)
result = createWordVector([result])
print(result)
