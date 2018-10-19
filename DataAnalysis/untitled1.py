from bs4 import BeautifulSoup
import urllib.request as rq
import requests
import lxml

url = "https://youtu.be/BzYnNdJhZQw?"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
#read = soup.select('div #info')

test = soup.find_all("div")
print(test)