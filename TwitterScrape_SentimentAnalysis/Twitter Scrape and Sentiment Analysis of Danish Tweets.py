#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import snscrape.modules.twitter as sntwitter
import pandas as pd
import re
import nltk
import emoji


# In[ ]:


## DOWNLOADING TWEETS
# Creating list to append tweet data to
tweets_list17 = []
#Choosing runtime of the tweets, and text search

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 OR covid19dk OR corona OR coronadk OR edpidemi OR pandemi OR virus since:2020-03-01 until:2021-04-01 lang:da').get_items()):
    tweets_list17.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.likeCount, tweet.retweetCount, tweet.mentionedUsers, tweet.lang, tweet.url ])
    
# Creating a dataframe from the tweets list above
tweets_list17 = pd.DataFrame(tweets_list17, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Likes', 'Retweets', "MentionedUsers", "Language", "Url"])

def cleaner(tweet):
    tweet = re.sub("@[A-Za-z0-9]+","",tweet) #Remove @ sign
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet) #Remove http links
    tweet = " ".join(tweet.split())
    tweet = tweet.replace("#", "").replace("_", " ") #Remove hashtag sign but keep the text
    return tweet

import re
def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)

tweets_list17['Tweet'] = tweets_list17['Text'].map(lambda x: cleaner(x))

tweets_list17['Tweet_NO_EMOJ'] = tweets_list17['Tweet'].map(lambda x: remove_emojis(x))

from langdetect import detect
tweets_list17['LangDetect'] =tweets_list17['Tweet_NO_EMOJ'].apply(detect)
tweets_list17 = tweets_list17.loc[tweets_list17['LangDetect'] == 'da']


# In[ ]:


#Using Bert Tone 
from danlp.models import load_bert_tone_model
classifier_to = load_bert_tone_model()
tweets_list17['Bert_Polarity'] = tweets_list17['Tweet'].apply(classifier_to.predict)


# In[19]:


#Using Bert Emotion
tweet_test1 = pd.read_csv("tweet_test1.csv")

from danlp.models import load_bert_emotion_model
classifier_da = load_bert_emotion_model()
Bert_E = tweet_test1['Tweet'].apply(classifier_da.predict)
tweet_test1 = tweet_test1.assign(Bert_Emotion=Bert_E.values) # assign values to column 'c'


# In[ ]:


#Saving Tweet list with analysis
tweet_list_Danmark.to_csv("tweet_list_Danmark_1.csv", index = False)

