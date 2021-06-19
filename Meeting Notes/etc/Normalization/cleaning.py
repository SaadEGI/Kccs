import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize


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


input_str = "\t \nThis &is [an] 2 33 example? {of} string. with.? 45 4 punctuation!!!!" # Sample string



# Replace digits with space
input_str = re.sub(r"\d+", "", input_str)
# Remove punctuations, instead put spaces
result = input_str.translate(str.maketrans("", "", string.punctuation))
#cleaning up
result = re.sub(' +', ' ', result)
# remove whitespaces (tabs,..)
result = result.strip()

print(result)

# input_str = "NLTK is a leading platform for building Python programs to work with human language data."
stop_words = set(stopwords.words('english'))

tokens = word_tokenize(result)
result = [i for i in tokens if not i in stop_words]
result =  " ".join(result)
print (result)

print(stemSentence(result))

