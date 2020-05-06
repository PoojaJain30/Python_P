#All imports
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import smtplib

#All variables declaration 
handle = input('Enter the twitter handle to get data: ')
data = {}
#Get the response content from tweeter
def is_good_response(res):
    content_type = res.headers['Content-Type'].lower()
    return (res.status_code == 200 and content_type is not None and content_type.find('html') > -1)

def get_response(url):
    try:
        response = requests.get(url)
        if is_good_response(response):
            return response.content
        else:
            return None
    except HTTPError as err:
        print(f'Http error occured: {err}')
        return None
    except Exception as otherErr:
        print(f'Other error occured: "{otherErr}')
        return None


#Get the required data from tweeter
def get_twitter_data(response):
    global data
    html = BeautifulSoup(response,'html.parser')
    #Following
    data['following'] = html.findAll(attrs={"data-nav": "following"})[0].findAll('span',class_='ProfileNav-value')[0].get('data-count')
    #Follower
    data['followers'] = html.findAll(attrs={"data-nav": "followers"})[0].findAll('span',class_='ProfileNav-value')[0].get('data-count')
    #Liked
    data['liked'] = html.findAll('li',class_='ProfileNav-item--favorites')[0].findAll('span',class_='ProfileNav-value')[0].get('data-count')
    #Tweets
    data['tweets'] = html.findAll('li',class_='ProfileNav-item--tweets')[0].findAll('span',class_='ProfileNav-value')[0].get('data-count')
    return data
#Sending data via email 

#final calls
response = get_response('https://twitter.com/'+ handle)
if response is not None:
    print(get_twitter_data(response))