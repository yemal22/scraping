from pprint import pprint

import requests
from bs4 import BeautifulSoup

# url = "https://books.toscrape.com/"
# response = requests.get(url)

# with open('books_to_scrap.html', 'w') as f:
#    f.write(response.text)

with open ('books_to_scrap.html', 'r') as f:
    file = f.read()

soup = BeautifulSoup(file, 'html.parser')

#articles = soup.find_all('article', class_='product_pod')
#for article in articles:
#    links = article.find_all('a')
#    if len(links) >= 2:
#        link = links[1]
#        print(link.get('title'))

titles = [a.get('title') for a in soup.find_all('a', title=True)]
pprint(titles)