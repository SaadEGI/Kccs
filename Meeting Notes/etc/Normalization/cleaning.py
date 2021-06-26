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


# You may need to download gensim before: pip install gensim
# from numpy import dot
import numpy as np 
from scipy.stats import norm
import warnings
warnings.filterwarnings(action = 'ignore')
import gensim
from gensim import models
from gensim.test.utils import common_texts
from gensim.models import Word2Vec


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
    sentence = sentence.lower()
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

# measure the similarity of 2 vectors using the angle teta between them
def cosine_distance (model, word,target_list , num) :
    cosine_dict ={}
    word_list = []
    a = model.wv[word]
    for item in target_list :
        if item != word :
            b = model.wv[item]
            cos_sim = np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
            cosine_dict[item] = cos_sim
    dist_sort = sorted(cosine_dict.items(), key=lambda dist: dist[1],reverse = True) ## in Descedning order 
    for item in dist_sort:
        word_list.append((item[0], item[1]))
    return word_list[0:num]



document = '''\t \nThis &is [an] 2 33 example? {of} string. with.? 45 4 punctuation!!!! try to add more than
one sentence to be able to illustrate the effect example.
''' # Sample string

print(document)
result = stemSentence(normatizeDocument(document))
print(result)
data = result
result = createWordVector([result])
print('count: ', result)


# Create CBOW model

corpus = [[word.lower() for word in data.split()]] # List the data checking lowercase
print('From str to list: ', corpus)


model = Word2Vec(corpus, min_count=1)
# print(model.wv.most_similar('exampl'))
print('Cos distance: ', cosine_distance (model,'add',['exampl', 'abl'],3)) 
