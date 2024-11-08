from pprint import pprint
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

with requests.Session() as session:

    response = session.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    categories_div = soup.find('div', class_='side_categories').find('ul').find('li').find('ul')
    categories = []
    for category in categories_div.children:
        if category.name:
            cat = {
                'name': category.text.strip(),
                'link': url + category.find('a').get('href')
            }
            categories.append(cat)

    for category in categories:
        req = session.get(category['link'])
        soup2 = BeautifulSoup(req.text, 'html.parser')
        nb = soup2.find('form', class_='form-horizontal').find('strong').text.strip()
        category['n_books'] = nb

    for category in categories:
        if int(category['n_books']) <=5:
            pprint(category)