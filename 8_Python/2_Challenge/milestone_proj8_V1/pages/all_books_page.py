import re
from logger_config import logger
from bs4 import BeautifulSoup
from parsers.book_parser import BookParser
from locators.all_books_page import AllBooksPageLocators

class AllBooksPage:
    def __init__(self, page_content):
        logger.debug('Parsing page content with BeautifulSoap HTML parser.')
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        #logger.debug(f'All books page locators using: {AllBooksPageLocators.BOOKS}')
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]
    
    @property
    def page_count(self):
        logger.debug('Finding all number of pages available...')
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        return pages
    