import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.example.com')
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find('h1').string)
print(soup.select_one('p a').attrs['href'])