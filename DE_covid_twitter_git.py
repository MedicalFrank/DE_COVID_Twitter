import tweepy #Twitter (pip install tweepy in command line)
import time

auth = tweepy.OAuthHandler('','') #API key is first, then API key secert is second
auth.set_access_token('','') #Acess token, Access token secret is the order


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) #wait_on_rate_limit will take a break when you are making too many api requests
user = api.me()

numberTweets = 500


for tweet in tweepy.Cursor(api.search, q="(Delaware AND COVID) OR (Delaware AND Coronavirus) OR (deCOVID) OR (coronavirusdelaware) OR (Delaware AND FlattenTheCurve) OR (socialdistancing AND Delaware) OR (netDE AND COVID) OR (netDE AND Coronavirus) OR (inWilm and COVID) OR (inWilm and Coronavirus) OR (#WilmDE and COVID) OR (#WilmDE and Coronavirus) -(Ohio OR 'Delaware Valley' OR 'Delaware County' OR 'Delaware River')", lang="en", ).items(numberTweets):
    try:
        print('Tweet Retweeted')
        tweet.retweet()
        time.sleep(180)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
