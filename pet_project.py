import requests
from bs4 import BeautifulSoup
import csv
import time


source = requests.get("https://store.steampowered.com/search/?specials=1").text


soup = BeautifulSoup(source, "html5lib")

# csv_file = open('steam_scrape.csv', 'w')


print('\n')

for discounts in soup.find_all('a', class_ = 'search_result_row'):
    time.sleep(2)
    
    name = discounts.find('span', class_='title').text
    print(name + '\n')

    on_sale = discounts.find('div', class_='search_discount').span.text
    print(on_sale)

    price = discounts.find('div', class_= 'search_price').text
    print('Original price\tOn sale price')

    price = price.replace('\n\t\t\t\t\t\t\t\t', '')
    price = price.replace('€', '€\t\t')
    # for letter in price:
    #     if letter
    print(price)
    print('\n')

# print(soup.prettify())

# discounts = soup.find('search_discount')

# response = requests.get(url)

# text = response.text

# print(text)
