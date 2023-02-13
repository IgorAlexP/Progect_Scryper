import requests
from bs4 import BeautifulSoup
import lxml

url = "https://service.gadgetufa.ru/remont-samsung/samsung-galaxy-a/"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

soup_name = soup.findAll('div', class_='SubCategory')#.find('div', class_= 'Name')
soup_price = soup.find('div', class_='Services').find('div', class_= 'Price')
print(soup_name)  
print(soup_price)