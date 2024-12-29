from selenium import webdriver
from pages.quote_page import QuotePage, InvalidTagSelectionException

try:
    author = input("Enter the author you'd like quotes from: ")
    tag = input("Enter your tag:")

    chrome = webdriver.Chrome()
    chrome.get('http://quotes.toscrape.com/search.aspx')
    page = QuotePage(chrome)

    print(page.search_for_quotes(author, tag))
except InvalidTagSelectionException as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown error occurred. Please try again.") 
