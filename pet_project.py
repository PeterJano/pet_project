import requests
from bs4 import BeautifulSoup
import csv
import time


source = requests.get("https://store.steampowered.com/search/?specials=1").text


soup = BeautifulSoup(source, "html5lib")

# csv_file = open('steam_scrape.csv', 'w')


for discounts in soup.find_all('a', class_ = 'search_result_row'):
    time.sleep(2)
    
    name = discounts.find('span', class_='title').text
    print(name)

    on_sale = discounts.find('div', class_='search_discount').span.text
    print(on_sale)

    price = discounts.find('div', class_= 'search_price').text
    for letter in price:
        if letter
    print(price.split('€'))

# print(soup.prettify())

# discounts = soup.find('search_discount')

# response = requests.get(url)

# text = response.text

# print(text)
