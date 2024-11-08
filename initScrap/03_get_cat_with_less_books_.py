from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/index.html"

def main(threshold : int = 5):
    with requests.Session() as session:
        response = session.get(BASE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        categories = soup.select("ul.nav.nav-list a")
        categories_url = [ urljoin(BASE_URL, category["href"]) for category in categories[1:]]

        for category in categories_url:
            response = session.get(category)
            soup = BeautifulSoup(response.text, 'html.parser')

            number_of_books = len(soup.select("article.product_pod"))
            category_name = soup.select_one("h1").text
            if number_of_books <= threshold:
                print(f"La catégorie '{category_name}' ne contient pas assez de livres ({number_of_books}).")
            else:
                print(f"La catégorie '{category_name}' contient assez de livre.")

if __name__ == '__main__':
    main(threshold=15)