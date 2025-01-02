import aiohttp
import asyncio

async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status)
            return response.status
        
loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_page('http://books.toscrape.com')) # This is a blocking call