from selenium import webdriver
from pages.quote_page import QuotePage

chrome = webdriver.Chrome()
chrome.get('http://quotes.toscrape.com/search.aspx')
page = QuotePage(chrome)

author = input("Enter the author you'd like quotes from: ")
page.select_author(author) # The QuotePage class has a method select_author

tags = page.get_avaiable_tags()
print("Select one of these tags: [{}]".format(" | ".join(tags)))

selected_tag = input("Enter your tag:")
page.select_tag(selected_tag)

page.search_button.click()
print(page.quotes)