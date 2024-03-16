import requests
from bs4 import BeautifulSoup
import pandas as pd

productslinks = []

for i in range(1, 15):
    r = requests.get(f'https://www.alkoholeswiata.com/rodzaj/alkohole-mocne/whisky/whisky-kraj-whisky-szkocka/page/{i}/')
    soup = BeautifulSoup(r.content, 'html.parser')
    productlist = soup.find_all('li', {'class': 'product'})

    for item in productlist:
        for link in item.find_all('a', href=True):
            productslinks.append(link['href'])

whiskeylist = []

for link in productslinks[:5]:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')

    title = soup.find('h1', {'class': 'product_title'}).text
    price = soup.find('p', {'class': 'price'}).text
    try:
        rating = soup.find('strong', {'class': 'rating'}).text
    except:
        rating = 'No rating'

    data = {
        'title': title,
        'price': price,
        'rating': rating
    }

    whiskeylist.append(data)

dt = pd.DataFrame(whiskeylist)
dt.to_excel('whisky.xlsx')