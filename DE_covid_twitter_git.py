import tweepy #Twitter (pip install tweepy in command line)
import time
import bs4
import requests

auth = tweepy.OAuthHandler('','') #API key is first, then API key secert is second
auth.set_access_token('','') #Acess token, Access token secret is the order


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) #wait_on_rate_limit will take a break when you are making too many api requests
user = api.me()

numberTweets = 500

def get_DE_COVID_Case (NYTUrl):
    res = requests.get(NYTUrl)
    # must program in a get request that pulls info peroidically
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#cases-top-presentation > div.g-asset.g-svelte.top-counts.g-asset-width-full > div > div > div:nth-child(1) > div.num.svelte-ath6yh')
    return elems[0].text

#DEcasecount = get_DE_COVID_Case ('https://www.nytimes.com/interactive/2020/us/delaware-coronavirus-cases.html')

#print('The total COVID-19 cases in Delaware, USA are ' + DEcasecount)
#api.update_status('The total COVID-19 cases, according to @nytimes, in Delaware, USA are ' + DEcasecount + '.')

for tweet in tweepy.Cursor(api.search, q="(Delaware AND COVID) OR (Delaware AND Coronavirus) OR (deCOVID) OR (coronavirusdelaware) OR (Delaware AND FlattenTheCurve) OR (socialdistancing AND Delaware) OR (netDE AND COVID) OR (netDE AND Coronavirus) OR (inWilm and COVID) OR (inWilm and Coronavirus) OR (#WilmDE and COVID) OR (#WilmDE and Coronavirus) -(Ohio OR 'Delaware Valley' OR 'Delaware County' OR 'Delaware River')", lang="en", ).items(numberTweets):
    try:
        print('Tweet Retweeted')
        tweet.retweet()
        time.sleep(180)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
