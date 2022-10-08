# Botometer Test
This file only has 1 test which is to check whether or not the program could make a query using provided test values. This was done (and not more custom tests) as Botometer 
apparently does NOT support the Twitter V2 API, but the Twitter V1.1 API (which it was built around). The process to access the V1.1 API takes weeks so, I decided to just
test the API with the only call that I could make. 

## Results
The result of that test was successful as I was able to query the test data using my API key. But more importantly, figuring out what version of the Twitter API Botometer 
is built around (or at least the library that they povide to make querying much easier than filling out an entire HTTP body and header).

# Twitter API Tests
In this file, I do not use the Twitter API directly as the documentation did not cover everything and the documentation that was provided didn't go far enough 
(e.g rarely provided examples on how to use the API, like authentification to use the API). So, I used a python wrapper that interacts with the Twitter API for me
(the developer of the wrapper is credited in a comment in the test file). So using that wrapper, I tested various functions like searching up a user, searching for tweets 
and searching for followers. For the test account, I used the NY Mets Twitter account. 

## Results
For the results, I was able to look up the NY Mets account and was able to pull their user ID value. For the followers test, I was able to pull the amount of followers
that I wanted, however I do not know if the followers that are returned are in chronological order. They could be the last X followers, the first X followers or just a 
random selection of X users. For pulling tweets, I was able to pull a specified amount of them accoarding to the tweet ID. I can't specify an exact amount of tweets to pull 
given the first/last tweet in a time frame as it justs pull them all.

# Google NLP Tests
For these tests, I focused on the sentiment analysis API. I ran roughly 7 different tests that each had a different sentence to analyze. I tried to make each sentence have 
a different sentiment. Meaning that some of the sentences were very postive, some were negative and some were neutral. I did this to see what kinds of metrics Google uses
to do sentiment analysis and to see if sentences with similar sentiments had similar ratings.

## Results
From what I can tell, Google gives 2 values that represent the sentiment of the given text. The closer both values are to +1, the more positive the sentiment is. This also
means that the closer those values are to -1, the more negative the sentiment is. Factual statements seem to be neutral, which is what I expect (both values are close to 0) 
and common positive phrases such as 'Happy birthday' have a high value for sentiment analysis.
