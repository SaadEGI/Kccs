from collections import Counter
from collections import defaultdict


import matplotlib.pyplot as plt
import nltk
import numpy as np
import pandas as pd
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis
import gensim

import seaborn as sns
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud

news = pd.read_csv('30k_tweets_Dataset.csv', error_bad_lines=False)
news.head(3)

news['fulltext'].str.len().hist()

news['fulltext'].str.split(). \
    apply(lambda x: [len(i) for i in x]). \
    map(lambda x: np.mean(x)).hist()



nltk.download('stopwords')



nltk.download('stopwords')
stop = set(stopwords.words('english'))
corpus = []
new = news['fulltext'].str.split()
new = new.values.tolist()
corpus = [word for i in new for word in i]



dic = defaultdict(int)
for word in corpus:
    if word in stop:
        dic[word] += 1



top = sorted(dic.items(), key=lambda x: x[1], reverse=True)[:15]
x, y = zip(*top)
plt.bar(x, y)





counter = Counter(corpus)
most = counter.most_common()

x, y = [], []
for word, count in most[:40]:
    if (word not in stop):
        x.append(word)
        y.append(count)

sns.barplot(x=y, y=x)



def get_top_ngram(corpus, n=None):
    vec = CountVectorizer(ngram_range=(n, n)).fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx])
                  for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq[:10]


top_n_bigrams = get_top_ngram(news['fulltext'], 2)[:10]
x, y = map(list, zip(*top_n_bigrams))
sns.barplot(x=y, y=x)

top_tri_grams = get_top_ngram(news['fulltext'], n=3)
x, y = map(list, zip(*top_tri_grams))
sns.barplot(x=y, y=x)



nltk.download('punkt')
nltk.download('wordnet')


def preprocess_news(df):
    corpus = []
    stem = PorterStemmer()
    lem = WordNetLemmatizer()
    for news in df['fulltext']:
        words = [w for w in word_tokenize(news) if (w not in stop)]

        words = [lem.lemmatize(w) for w in words if len(w) > 2]

        corpus.append(words)
    return corpus


corpus = preprocess_news(news)

dic = gensim.corpora.Dictionary(corpus)
bow_corpus = [dic.doc2bow(doc) for doc in corpus]

lda_model = gensim.models.LdaMulticore(bow_corpus,
                                       num_topics=4,
                                       id2word=dic,
                                       passes=10,
                                       workers=2)
lda_model.show_topics()


pyLDAvis.enable_notebook()
vis = gensimvis.prepare(lda_model, bow_corpus, dic)
vis



stopwords = set(STOPWORDS)


def show_wordcloud(data):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=100,
        max_font_size=30,
        scale=3,
        random_state=1)

    wordcloud = wordcloud.generate(str(data))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')

    plt.imshow(wordcloud)
    plt.show()


show_wordcloud(corpus)


nlp = spacy.load("en_core_web_sm")


doc = nlp('India and Iran have agreed to boost the economic viability \
of the strategic Chabahar port through various measures, \
including larger subsidies to merchant shipping firms using the facility, \
people familiar with the development said on Thursday.')

[(x.text, x.label_) for x in doc.ents]



displacy.render(doc, style='ent', jupyter=True)


def ner(text):
    doc = nlp(text)
    return [X.label_ for X in doc.ents]


ent = news['fulltext']. \
    apply(lambda x: ner(x))
ent = [x for sub in ent for x in sub]

counter = Counter(ent)
count = counter.most_common()

tweetx, y = map(list, zip(*count))
sns.barplot(x=y, y=x)


def ner(text, ent="GPE"):
    doc = nlp(text)
    return [X.text for X in doc.ents if X.label_ == ent]


gpe = news['fulltext'].apply(lambda x: ner(x))
gpe = [i for x in gpe for i in x]
counter = Counter(gpe)

x, y = map(list, zip(*counter.most_common(10)))
sns.barplot(y, x)

per = news['fulltext'].apply(lambda x: ner(x, "PERSON"))
per = [i for x in per for i in x]
counter = Counter(per)

x, y = map(list, zip(*counter.most_common(10)))
sns.barplot(y, x)

org = news['fulltext'].apply(lambda x: ner(x, "ORG"))
org = [i for x in org for i in x]
counter = Counter(org)

x, y = map(list, zip(*counter.most_common(10)))
sns.barplot(y, x)