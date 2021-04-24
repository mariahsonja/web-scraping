import requests
from bs4 import BeautifulSoup

url = requests.get('http://books.toscrape.com/')
soup = BeautifulSoup(url.text, 'html.parser')

href_list = []
links = soup.find_all('a')
for link in links:
    fullLink = link.get('href')
    href_list.append(fullLink)

print(href_list)
