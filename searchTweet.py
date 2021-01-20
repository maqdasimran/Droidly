import tweepy
import time
#Consumer keys and ID have been hidden 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

hashtag = '#'
tweetnumber = 10
tweets = tweepy.Cursor(api.search, hashtag).items(tweetnumber)
def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)
searchBot()