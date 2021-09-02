import nltk # Python library for NLP
from nltk.corpus import twitter_samples # sample Twitter dataset from NLTK
import matplotlib.pyplot as plt # library for visualization
import random

nltk.download('twitter_samples')

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

# print('Number of positive tweets: ', len(all_positive_tweets))
# print('Number of negative tweets: ', len(all_negative_tweets))
# print('\nThe type of all_positive_tweets is: ', type(all_positive_tweets))
# print('The type of a tweet entry is: ', type(all_negative_tweets[0]))

# # Declare a figure with a custom size
# fig = plt.figure(figsize=(5, 5))
# # labels for the classes
# labels = 'ML-BSB-Lec', 'ML-HAP-Lec','ML-HAP-Lab'
# # [nltk_data] Downloading package twitter_samples to /root/nltk_data...
# # [nltk_data] Unzipping corpora/twitter_samples.zip.
# # Out[2]:
# # # True

# # Number of positive tweets: 5000
# # Number of negative tweets: 5000
# # The type of all_positive_tweets is: <class 'list'>
# # The type of a tweet entry is: <class 'str'>

# # Sizes for each slide
# sizes = [40, 35, 25]
# # Declare pie chart, where the slices will be ordered and plotted counter-clockwise:
# plt.pie(sizes, labels=labels, autopct='%.2f%%',
# shadow=True, startangle=90)
# #autopct enables you to display the percent value using Python string formatting.
# #For example, if autopct='%.2f', then for each pie wedge, the format string is '%.2f' and

# # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.axis('equal')
# # Display the chart
# plt.show()

# Declare a figure with a custom size
# fig = plt.figure(figsize=(5, 5))
# # labels for the two classes
# labels = 'Positives', 'Negative'
# # Sizes for each slide
# sizes = [len(all_positive_tweets), len(all_negative_tweets)]
# # Declare pie chart, where the slices will be ordered and plotted counter-clockwise:
# plt.pie(sizes, labels=labels, autopct='%1.1f%%',
# shadow=True, startangle=90)
# # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.axis('equal')
# # Display the chart
# plt.show()

print('\033[92m' + all_positive_tweets[random.randint(0,5000)])
# print negative in red
print('\033[91m' + all_negative_tweets[random.randint(0,5000)])

tweet = all_positive_tweets[2277]
print(tweet)

nltk.download('stopwords')

import re # library for regular expression operations
import string # for string operations
from nltk.corpus import stopwords # module for stop words that come with NLTK
from nltk.stem import PorterStemmer # module for stemming
from nltk.tokenize import TweetTokenizer

print('\033[92m' + tweet)
print('\033[94m')
# remove hyperlinks
tweet2 = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
# remove hashtags
# only removing the hash # sign from the word
tweet2 = re.sub(r'#', '', tweet2)
print(tweet2)

print()
print('\033[92m' + tweet2)
print('\033[94m')
# instantiate tokenizer class
tokenizer = TweetTokenizer(preserve_case=False)
# tokenize tweets
tweet_tokens = tokenizer.tokenize(tweet2)
print()
print('Tokenized string:')
print(tweet_tokens)

stopwords_english = stopwords.words('english')
print('Stop words\n')
print(stopwords_english)
print('\nPunctuation\n')
print(string.punctuation)