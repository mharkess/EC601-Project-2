from getpass import getuser
from urllib import response
import tweepy
import os
import json
from google.cloud import language_v1
from dotenv import load_dotenv

#Load keys to access API
load_dotenv()

client = tweepy.Client(os.getenv("twitter_bearer_token"))

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "D:\emerald-entity-261417-fe12db424058.json"
googleClient = language_v1.LanguageServiceClient()

MAX_RESULTS = 20

def getUserID(twitterUserName):
   response = client.get_user(username = twitterUserName)
   return response.data.id

def getMentions(userID):
   response = client.get_users_mentions(id = userID, max_results = MAX_RESULTS)
   return response.data

def getSentiment(tweet):
   document = language_v1.Document(
    content=tweet, type_=language_v1.Document.Type.PLAIN_TEXT
    )
    # Detects the sentiment of the text
   sentiment = googleClient.analyze_sentiment(
   request={"document": document}
    ).document_sentiment

   print("Text: {}".format(tweet))
   print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))
   return sentiment

def getSentimentText(user):
   resp = getMentions(getUserID(user))
   tweetdisplay = ''
   for tweet in resp:
      tweetdisplay = tweetdisplay + tweet.text + '\n' + '\n'
   return tweetdisplay


def sentimentList(list):
   sentiments = []
   for tweet in list:
      sentiments.append(getSentiment(tweet.text))
   return sentiments



def getAvgSentiment(username):
   idelon = getUserID(username)
   tweets = getMentions(idelon)
   sentiments = sentimentList(tweets)
   avgSentiment = 0
   for nlp in sentiments:
      avgSentiment += nlp.score
   avgSentiment = avgSentiment / MAX_RESULTS
   return(str(avgSentiment))
