import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.c/"
web = requests.get(url)
soup = BeautifulSoup(web.text,'lxml')
enlaces = soup.find_all('ul').find_all('a')

