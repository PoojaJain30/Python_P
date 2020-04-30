import requests
from bs4 import BeautifulSoup
print("file execss")
URL = 'https://www.learningcaregroup.com/about-us/weekly-activities/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')  
print(soup) 