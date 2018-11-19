from nltk.stem.wordnet import WordNetLemmatizer 
from nltk.stem.porter import PorterStemmer 
import nltk
# question 1
word1 = "studies"
word2 = "studying"
stem = PorterStemmer()
lem = WordNetLemmatizer()

# print('Original Word studies (stem) : '
# ,stem.stem(word1))
# print('Original Word studies (lemm) : '
# ,lem.lemmatize(word1,"v"))

# print('Original Word studying (stem) : '
# ,stem.stem(word2))
# print('Original Word studying (lemm): '
# ,lem.lemmatize(word2,"v"))


# quesiton 2
from nltk.tokenize import word_tokenize
sentence = "Analytics Vidhya is a great source  \
to learn data science"
tokens = nltk.word_tokenize(sentence)
bigrm = list(nltk.bigrams(tokens))
count = 1
# for x in bigrm:
#     print(count, x)
#     count = count + 1

# question 3
# import string
# from nltk.corpus import stopwords
# import re
# from nltk.tokenize import word_tokenize
# from nltk.util import ngrams
# print(string.punctuation)
# print()

# word_list = "#Analytics-vidhya is a great source to learn @data_science."
# word_list = word_tokenize(word_list)
# filtered_words = [word for word in word_list if word not in stopwords.words('english')]
# print("Original: ", ' '.join(word_list))
# print()
# print("Remove Stop Word: ", ' '.join(filtered_words))
# print()
# regex = re.compile('[%s]' % re.escape(string.punctuation))
# out = regex.sub(' ', ' '.join(filtered_words))
# print("Replace punctuation: ", out)






# question 4
import re
given_sen = "The next meetup on data science will be held on 2017-09-21, \
 previously it happened on 31/03, 2016"

one = re.search('\d{4}-\d{2}-\d{2}',given_sen)
print(one)
two = re.match('(19|20)\d{2}-(0[1-9]|1[0-2])-[0-2][1-9]',given_sen)
print(two)
three = re.match('(19|20)\d{2}-(0[1-9]|1[0-2])-([0-2][1-9]|3[0-1])',given_sen)
print(three)

m = re.findall('\d{4}-\d{2}-\d{2}|\d{2}/\d{2}, \d{4}', given_sen)
print(m)


# -- end code --