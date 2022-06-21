import requests
from bs4 import BeautifulSoup


def web_crawler(max_page):
    page = 0
    while max_page > page:
        url = 'http://books.toscrape.com/catalogue/category/books_1/page-' + str(page) + '.html'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('h3'):
            href = link('href')
            title = link.string
            print(href)
            print(title)
        page += 1


print(web_crawler(2))