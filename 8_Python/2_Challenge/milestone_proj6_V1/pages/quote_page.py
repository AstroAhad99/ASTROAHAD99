from typing import List
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from locators.quotes_page_locators import QuotePageLocators
from parsers.quote import QuoteParser

class QuotePage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        locator = QuotePageLocators.QUOTE
        quote_tags = self.browser.find_elements(By.CSS_SELECTOR, locator)
        return [QuoteParser(tag) for tag in quote_tags]
    
    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element(By.CSS_SELECTOR, QuotePageLocators.AUTHOR_DROPDOWN)
        return Select(element)
    
    @property
    def tag_dropdown(self) -> Select:
        element = self.browser.find_element(By.CSS_SELECTOR, QuotePageLocators.TAG_DROPDOWN)
        return Select(element)
    
    @property
    def search_button(self):
        return self.browser.find_element(By.CSS_SELECTOR, QuotePageLocators.SEARCH_BUTTON)

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    def get_avaiable_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tag_dropdown.options]
    
    def select_tag(self, tag_name: str):
        self.tag_dropdown.select_by_visible_text(tag_name)

    
