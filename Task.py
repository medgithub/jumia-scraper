import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv


url = 'https://www.jumia.ma/telephones-portables/?page='



for page in range(3):
    print('---', page, '---')
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    ancher=soup.find_all('div',{'class' : "sku -gallery"})


    for pt in  ancher:
        name = pt.find('span', {'class': 'name'})
        price = pt.find('span', {'class': 'price'})
        brand = pt.find('span', {'class': 'brand'})
        img = pt.find('img')['data-src']
##        if pt.find('img')['src']:
##            images = pt.find('img')['src']
##            print images
        print('--------------------------------------------------')
        print('Title :' + name.text.replace('                    ', '').strip('\r\n'))
        print('image : ' + img)
        print('Price : ' + price.text)
        print('brand : ' + brand.text.replace('                    ', '').strip('\r\n'))  
        print('--------------------------------------------------')
