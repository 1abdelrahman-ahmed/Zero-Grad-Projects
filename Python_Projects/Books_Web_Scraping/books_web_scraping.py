import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_categories():
    base_url = 'https://books.toscrape.com/'
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'lxml')
    categories = soup.find('ul', class_='nav nav-list').find('ul').find_all('li')
    categories_cleaned = [category.a.text.strip() for category in categories]
    categories_simplified = [category.lower().replace(' ', '-') + '_' + str(i+2) for i, category in enumerate(categories_cleaned)]
    return {k: v for k, v in zip(categories_cleaned, categories_simplified)}

def get_category_url(category):
    base_url = 'https://books.toscrape.com/catalogue/category/books/'
    category_key = get_categories().get(category)
    if category_key:
        return f'{base_url}{category_key}/index.html'
    else:
        raise ValueError(f'Category "{category}" not found in the dictionary.')

def scrape_books(category):
    try:
        url = get_category_url(category)
    except ValueError as e:
        print(e)
        return None
    else:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')

        num_of_books = int(soup.find_all('strong')[1].text)
        num_of_pages = num_of_books // 20 + num_of_books % 20

        all_books_df = pd.DataFrame()

        for page in range(1, num_of_pages + 1):
            if page == 1:
                page_url = url
            else:
                page_url = f'{url[:-10]}page-{page}.html'

            response = requests.get(page_url)
            soup = BeautifulSoup(response.content, 'lxml')

            names = soup.find_all('h3')
            names_lst = [name.a['title'] for name in names]

            prices = soup.find_all('p', 'price_color')
            prices_lst = [price.text.strip('£') for price in prices]

            ratings = soup.find_all('p', 'star-rating')
            ratings_lst =  [rating['class'][1] for rating in ratings]
            rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
            ratings_lst =  [rating_map[rating] for rating in ratings_lst]

            books_dict = {
                'Book Name': names_lst,
                'Price': prices_lst,
                'Rating': ratings_lst
            }

            books_df = pd.DataFrame(books_dict)

            all_books_df = pd.concat([all_books_df, books_df], ignore_index=True)

        return all_books_df