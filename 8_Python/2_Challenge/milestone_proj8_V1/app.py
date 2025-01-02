import requests
import aiohttp
import asyncio
import async_timeout
import time

from logger_config import logger
from pages.all_books_page import AllBooksPage
loop = asyncio.get_event_loop()

logger.info('loading books list...')

page_content = requests.get('http://books.toscrape.com').content
page = AllBooksPage(page_content)
books = page.books

urls = [f"http://books.toscrape.com/catalogue/page-{page_num+1}.html" for page_num in range(1, page.page_count)]

async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f"Page took {time.time() - page_start}")
            return await response.text()
    
async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f"All took {time.time() - start}")

for page_content in pages:
    logger.debug('Creating AllBooksPage from page content.')
    page = AllBooksPage(page_content)
    books.extend(page.books)