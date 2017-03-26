#File Name: twitterSentmtAlysis.py

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sentiment_module as sm
import json


#consumer key, consumer secret, access token, access secret.
from twitterapiconnect import *

class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data['text']
        sentiment,confidence = sm.sentiments(tweet)
        # counter = counter + 1

        if confidence >= 80:         
        	out = open("twitter-out.txt","a")
        	out.write(sentiment)
        	out.write('\n')
        	out.close()
        	print(tweet.encode("utf-8"),sentiment,confidence)

        # if counter > 10:
        return(True)    

    def on_error(self, status):
        print (status)



auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

Stream = Stream(auth, listener())

def on_streaming(topic):
    # counter = 0
    Stream.filter(track=[topic])

on_streaming("meditation")