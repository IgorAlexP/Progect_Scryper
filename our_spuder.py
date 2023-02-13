import requests
from bs4 import BeautifulSoup
import lxml

url = "https://service.gadgetufa.ru/remont-samsung/samsung-galaxy-a/"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

print(soup.find('div', class_='Category'))