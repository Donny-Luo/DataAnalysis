from bs4 import BeautifulSoup
import requests

content = requests.get('https://books.toscrape.com/').text
soup = BeautifulSoup(content, "html.parser")
all_prices = soup.findAll('p', attrs={"class": "price_color"})
# print(soup.p)
for price in all_prices:
    print(price.string[1:])

all_titles = soup.findAll('h3')
for title in all_titles:
    all_links = title.findAll('a')
    for link in all_links:
        print(link.string)
