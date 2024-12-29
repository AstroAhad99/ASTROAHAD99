#from bs4 import BeautifulSoup

from locators.quotes_page_locators import QuotePageLocators
from parsers.quote import QuoteParser
from selenium.webdriver.common.by import By

class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self):
        locator = QuotePageLocators.QUOTE
        quote_tags = self.browser.find_elements(By.CSS_SELECTOR, locator)
        return [QuoteParser(tag) for tag in quote_tags]
