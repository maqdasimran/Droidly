import tweepy
import time
#Consumer keys and ID have been hidden 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
myFile ='last_seen.txt'



def checkSeen(myFile):
    firstFile = open(myFile, 'r')
    fileID = int(firstFile.read().strip())
    firstFile.close()
    return fileID

def checkLast(myFile, fileID):
    secondFile = open(myFile, 'w')
    secondFile.write(str(fileID))
    secondFile.close()
    return

def autoReply():
    tweets = api.mentions_timeline(checkSeen(myFile), tweet_mode= 'extended')
    for tweet in reversed(tweets):
        if '#' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + " Hello There", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            checkLast(myFile, tweet.id)

while True:
    autoReply()
    time.sleep(2)