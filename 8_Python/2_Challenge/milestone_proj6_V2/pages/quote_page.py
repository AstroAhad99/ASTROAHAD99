from typing import List
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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

    def search_for_quotes(self, author_name: str, tag_name: str):
        self.select_author(author_name)

        WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 
                                                            QuotePageLocators.TAG_DROPDOWN))
        )

        try:
            self.select_tag(tag_name)
        except NoSuchElementException:
            raise InvalidTagSelectionException(f"Tag '{tag_name}' not available for {author_name}")
        
        self.search_button.click()
        return self.quotes

class InvalidTagSelectionException(ValueError):
    pass