# Get data from the url using beutifulSoup and request
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

URL = 'https://www.learningcaregroup.com/about-us/weekly-activities/'


try:
    response = requests.get(URL)
except HTTPError as err:
    print(f'Http error occured: {err}')
except Exception as otherErr:
    print(f'Other error occured: "{otherErr}')
else:
    print('success')

html = BeautifulSoup(response.content, 'html.parser')  

heading = html.div.findAll('a')
print(heading)

for link in heading:
    print(link.get('href'))
    print(link.text)