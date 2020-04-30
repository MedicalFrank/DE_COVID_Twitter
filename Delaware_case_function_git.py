import tweepy
import bs4
import requests

auth = tweepy.OAuthHandler('','') #API key is first, then API key secert is second
auth.set_access_token('','') #Acess token, Access token secret is the order

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) #wait_on_rate_limit will take a break when you are making too many api requests
user = api.me()

def get_DE_COVID_Case (NYTUrl):
    res = requests.get(NYTUrl)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#cases-top-presentation > div.g-asset.g-svelte.top-counts.g-asset-width-full > div > div > div:nth-child(1) > div.num.svelte-1iocbin')
    return elems[0].text


DEcasecount = get_DE_COVID_Case ('https://www.nytimes.com/interactive/2020/us/delaware-coronavirus-cases.html')
print('The total COVID-19 cases, according to @nytimes, in Delaware, USA are ' + DEcasecount + '.')
api.update_status('The total COVID-19 cases, according to @nytimes, in Delaware, USA are ' + DEcasecount + '.')
