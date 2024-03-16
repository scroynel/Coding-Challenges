from requests_html import HTMLSession

url = 'https://www.beerwulf.com/en-gb/c/beer-kegs/blade-kegs'

s = HTMLSession()
r = s.get(url)

r.html.render(sleep=1)

products = r.html.xpath('//*[@id="product-items-container"]', first=True)
print(products.absolute_links)