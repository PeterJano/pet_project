import requests
import webbrowser
from bs4 import BeautifulSoup
import csv
import time
import sys
import os
import random
from PIL import Image


def menu(soup):

    choice = " "
    while choice not in '1 2 3 4 666'.split():
        os.system("clear")
        choice = input("{:>300}".format(" Choose an option!\n\n") +
                            "{:>295}".format("(1) Show all\n") +
                            "{:>302}".format("(2) Filter by price\n") +
                            "{:>301}".format("(3) Filter by sale\n") +
                            "{:>292}".format("(q) Quit\n\n"))

        if choice == "1":
            show_all(soup)  # Ide gyün a show all fgv.
        elif choice == "2":
            lowest_discount = input("Please enter the minimum desired discount: ")
            lowest_discount *= -1
            show_filtered_by_sale(soup, lowest_discount)  # Filter by price fgv.
        elif choice == "3":
            lowest_price = input("Please enter the minimum desired price: ") 
            show_filtered_by_price(soup, lowest_price)  # filter by sale
        elif choice == "q":
            sys.exit()
        elif choice == "666":
            easter_egg_1()


def easter_egg_1():
    # webbrowser.open_new("http://i.kym-cdn.com/photos/images/original/000/508/987/d12.gif")
    img = Image.open('filename.jpg')
    img.show()


def making_soup():
    source = requests.get("https://store.steampowered.com/search/?specials=1").text
    soup = BeautifulSoup(source, "html5lib")
    return soup


def show_all(soup):
    for discounts in soup.find_all('a', class_ = 'search_result_row'):
        time.sleep(random.randint(2,4))        

        name = discounts.find('span', class_='title').text
        on_sale = discounts.find('div', class_='search_discount').span.text
        price = discounts.find('div', class_= 'search_price').text


        print(name + '\n')
        print(on_sale)
        print('Original price\tOn sale price')
        price = price.replace('\n\t\t\t\t\t\t\t\t', '')
        price = price.replace('€', '€\t\t')
        print(price)
        print('\n')


def show_filtered_by_price(soup, number):
    for discounts in soup.find_all('a', class_ = 'search_result_row'):
        time.sleep(random.randint(2,4))
        on_sale = discounts.find('div', class_='search_discount').span.text
        name = discounts.find('span', class_='title').text
        price = discounts.find('div', class_= 'search_price').text
        price = price.replace('\n\t\t\t\t\t\t\t\t', '')
        price = price.replace('€', '€\t\t')
        rounded_price = price[0:2]
        if price >= number:
            continue
        
        print(name + '\n')
        print(on_sale)
        print('Original price\tOn sale price')
        print(price)
        print('\n')


def show_filtered_by_sale(soup, number):
    for discounts in soup.find_all('a', class_ = 'search_result_row'):
        time.sleep(random.randint(2,4))
        on_sale = discounts.find('div', class_='search_discount').span.text
        name = discounts.find('span', class_='title').text
        price = discounts.find('div', class_= 'search_price').text
        rounded_sale = on_sale[0:3]
        if rounded_sale >= number:
            continue
        
        price = price.replace('\n\t\t\t\t\t\t\t\t', '')
        price = price.replace('€', '€\t\t')
        print(name + '\n')
        print(on_sale)
        print('Original price\tOn sale price')
        print(price)
        print('\n')


def main():
    while True:

        soup = making_soup()
        menu(soup)


if __name__ == "__main__":
    main()




# csv_file = open('steam_scrape.csv', 'w')




# print(soup.prettify())

# discounts = soup.find('search_discount')

# response = requests.get(url)

# text = response.text

# print(text)
