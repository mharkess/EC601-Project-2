#twitter API V2 wrapper library: https://github.com/sns-sdks/python-twitter 

# Library imports
import requests
import os
from dotenv import load_dotenv
from pytwitter import Api


# Load keys to access API
load_dotenv()
twitter_api_cred = Api(
    consumer_key = os.getenv('twitter_consumer_key'), 
    consumer_secret = os.getenv('twitter_consumer_secret'),
    access_token = os.getenv('twitter_access_token'),
    access_secret = os.getenv('twitter_access_token_secret') 
    )

#Test 1 - Looking up user by username
resp = twitter_api_cred.get_user(username='Mets') #Should return NY Mets twitter account
print("Test 1")
print(resp)
print('----------------------------')

#Test 2 - Get a user's following base
resp = twitter_api_cred.get_followers(user_id = '39367703', max_results = 10) #Should be a list of users following the NY Mets
print("Test 2")
print(resp)
print('----------------------------')

#Test 3 - Looking up a user's tweets
resp = twitter_api_cred.get_tweets(["1578475848046637056","1578583735163056128"],expansions="author_id",tweet_fields=["created_at"], user_fields=["username","verified"]) #Should be a list of recent tweets by NY Mets
print("Test 3")
print(resp)
print('----------------------------')