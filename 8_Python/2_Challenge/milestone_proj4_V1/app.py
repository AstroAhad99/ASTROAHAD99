import requests

from logger_config import logger
from pages.all_books_page import AllBooksPage

logger.info('loading books list...')

page_content = requests.get('http://books.toscrape.com').content

page = AllBooksPage(page_content)

books = page.books

for page_num in range(1, page.page_count):
    url = f"http://books.toscrape.com/catalogue/page-{page_num+1}.html"
    page_content = requests.get(url).content
    page = AllBooksPage(page_content)
    books.extend(page.books)

