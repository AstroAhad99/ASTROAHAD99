"""
http://quotes.toscrape.com/


Projects:
app.py
quotes_page.py
quote.py

Locators:
quote_locators.py
quotes_page_locators.py

"""
#import requests
from selenium import webdriver
from pages.quotes_page import QuotesPage
chrome = webdriver.Chrome()


if __name__ == "__main__":
    #page_content = requests.get('http://quotes.toscrape.com/').content
    chrome.get('http://quotes.toscrape.com/')
    page = QuotesPage(chrome)
    for quote in page.quotes:
        print(quote)
