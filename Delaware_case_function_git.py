import tweepy
import bs4
import requests

auth = tweepy.OAuthHandler('','') #API key is first, then API key secert is second
auth.set_access_token('','') #Acess token, Access token secret is the order

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) #wait_on_rate_limit will take a break when you are making too many api requests
user = api.me()

def get_DE_COVID_Case (DHSSUrl):
    res = requests.get(DHSSUrl)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#overview > div > article > div > div > div.col-md-12.col-lg-6.d-flex.flex-column > div.c-dashboard-card.c-dashboard-card--simple.c-dashboard-card--stretch.mb-4 > div.c-dashboard-card__content-wrapper > div > div > div.c-summary-metric__group-wrapper.col-lg-12.col-xl-4.mb-4 > div > div.c-summary-metric__label-value-group > span.c-summary-metric__value.c-summary-metric__value--lg.d-block')
    return elems[0].text


DEcasecount = get_DE_COVID_Case ('https://myhealthycommunity.dhss.delaware.gov/locations/state')
print('The total COVID-19 cases, according to @Delaware_DHSS, in Delaware, USA are ' + DEcasecount + '.')
api.update_status('The total COVID-19 cases, according to @Delaware_DHSS, in Delaware, USA are' + DEcasecount+ '.')


