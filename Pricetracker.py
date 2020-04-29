#import bs4 as bs
#import urllib.request
#import requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

#source = urllib.request.urlopen('https://www.amazon.com/All-new-Kindle-Paperwhite-Waterproof-Storage/dp/B07PQ96B6B/ref=sr_1_7?crid=JMAXWL70TXQW&dchild=1&keywords=kindle%2Bfire&qid=1587680397&sprefix=kin%2Caps%2C165&sr=8-7&th=1').read()

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

#source = urllib.request.urlopen('https://www.amazon.com')
#mybytes = source.read()

#mystr = mybytes.decode("utf8")
#source.close()
raw_html = simple_get('https://www.amazon.com/')
print(len(raw_html))
#print(mystr)