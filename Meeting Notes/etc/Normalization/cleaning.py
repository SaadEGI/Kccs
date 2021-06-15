import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

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
print (result)
