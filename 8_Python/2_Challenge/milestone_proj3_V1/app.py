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

import requests
from pages.quotes_page import QuotesPage

if __name__ == "__main__":
    page_content = requests.get('http://quotes.toscrape.com/').content
    page = QuotesPage(page_content)
    for quote in page.quotes:
        print(quote.author)
