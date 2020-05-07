#All imports
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import smtplib

#All variables declaration 
handle = ''
data = {}
sender_email = 'poojapatil38@gmail.com'
password = ''
message = ''

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
def send_email(receiver_email,text,sender_email,password):
     try:
         smtpObj = smtplib.SMTP('smtp.gmail.com',587)
         smtpObj.ehlo()
         smtpObj.starttls()
         smtpObj.login(sender_email,password)
         smtpObj.sendmail(sender_email,receiver_email,text)
     except Exception as err:
         print(f'Error occured smtp: {err}')
     finally:
         smtpObj.quit()

#final calls
if __name__ == '__main__':
    handle = input('Enter the twitter handle to get data: ')
    password = input('Enter you email password: ')
    response = get_response('https://twitter.com/'+ handle)
    if response is not None:
        print(get_twitter_data(response))
        message = 'Subject: Your Twitter info\nDear '+handle+', \nYou have '+ data['followers']+'Followers and '+data['following']+' total following.\nYou liked '+data['liked']+' and total tweets so far is '+data['tweets']+'.\nThank you'
        print(message)
        send_email('ankit.jain08@gmail.com',message,sender_email,password)