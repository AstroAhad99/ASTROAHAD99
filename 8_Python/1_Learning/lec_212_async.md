1. The async programming involves few key concepts
2. Cooroutine, Await, and Event Loops
3. Async works on scheduling which means if one task is on waiting and taking time to execute then other function starts to operate.
4. Like while waiting for the server to respond with the data the program starts another task to execute.
5. Async works on concurrency (Not Parallelism) which means there are not multiprocessing rather than running the process on the single thread.
6. Real world applications for the Async are the 
    - Web scraping: For fetching multiple web pages
    - Chat servers: Establishing multiple client connections
    - File operation: Doing multiple read/write operations simultaneously
    - Darabase queries: Execute database queries concurrently
7. Libraries for async includes 
8. Key Libraries for Async Programming
    - asyncio: Core library for asynchronous programming in Python.Example: asyncio.sleep, asyncio.create_task, etc.
    - aiohttp: Asynchronous HTTP client/server.
    - asyncpg: Asynchronous PostgreSQL database driver.
    - httpx: Asynchronous HTTP client.
