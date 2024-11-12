import re

import requests
from bs4 import BeautifulSoup

def main() -> list[int]:

    book_ids = []

    try:
        response = requests.get("https://books.toscrape.com/index.html")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Il y a eu un problème lors de l'accès au site {e}")
        raise requests.exceptions.RequestException from e

    soup = BeautifulSoup(response.text, 'html.parser')
    one_star_books = soup.select("p.star-rating.One")
    for book in one_star_books:
        try:
            book_link = book.find_next("h3").find("a")["href"]
        except AttributeError as e:
            print(f"Impossible de trouver la balise '<h3>'.")
            raise AttributeError from e
        except TypeError as e:
            print("Impossible de trouver la balise '<a>' à l'intérieur de h3.")
            raise TypeError from e
        except KeyError as e:
            print("Impossible de trouver l'attribut 'href'.")
            raise KeyError from e

        try:
            book_id = re.findall(r"_\d+", book_link)[0][1:]
        except IndexError as e:
            print("Impossible de trouver l'id du livre.")
            raise IndexError from e
        else:
            book_ids.append(int(book_id))

    return book_ids

if __name__ == '__main__':
    print(main())