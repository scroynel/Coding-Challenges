import requests
from bs4 import BeautifulSoup
import pandas as pd

wine_list = []

# Step 1 - Request
def step_one(x):
    url = f'https://wanderlustwine.co.uk/buy-wine-online/page/{x}/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    return soup

# Step 2 - Parse
def parse(soup):
    products = soup.find_all('li', class_='product')
    for product in products:
        try:
            data = {
                'name': product.find('h2', class_='woocommerce-loop-product__title').text.strip(),
                'price': product.find('span', class_='price').text
            }
            wine_list.append(data)
        except:
            pass

# Step 3 - Output
def output():
    df = pd.DataFrame(wine_list)
    df.to_csv('wines.csv', index=False)


if __name__ == '__main__':
    for x in range(1, 24):
        print(f'Getting page {x}')
        html = step_one(x)
        print('Parsing...')
        parse(html)
    output()
    print('Saved to csv file.')