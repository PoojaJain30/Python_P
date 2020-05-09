# To get tOp 250 movies data and Save it as csv file
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import pandas as pd


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

#Data from imdb

def get_movie_info(res):
    html = BeautifulSoup(response,'html.parser')
    movies = html.findAll('td',class_="titleColumn")
    title,director,year,ratting = [],[],[],[]
    for movie in movies:
        title.append(movie.find('a').text) 
        director.append(movie.find('a').get('title'))
        year.append(movie.find('span').text)
        ratting.append(movie.findNext('td').text)
    return title,director,year,ratting

#main call
if __name__ == "__main__":
   response = get_response('https://www.imdb.com/chart/top')
   title,director,year,rattings = get_movie_info(response)
   df = pd.DataFrame({'Title':title,'Director':director,'Year':year,'Rattings':rattings})
   #changing the index to start from 1
   df.index = df.index + 1
   #removing the bracates from the years
   df['Year'] = df['Year'].map(lambda x:x.strip('()'))
   print(df.head(10))
   df.to_csv('top250movies.csv',index = True ,header = True)