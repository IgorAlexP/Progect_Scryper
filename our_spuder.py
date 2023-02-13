import requests
from bs4 import BeautifulSoup
import lxml

url = "https://service.gadgetufa.ru/remont-samsung/samsung-galaxy-a/"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
soup_name = soup.find('div', class_ ='flex-wrap').find('div', class_ = 'Name').find('a').text

soup = soup.find('div', class_ ='flex-wrap').find('div', class_ = 'Name').find('a').get('href')
link = "https://service.gadgetufa.ru" + soup
print(link)


print(soup_name)
