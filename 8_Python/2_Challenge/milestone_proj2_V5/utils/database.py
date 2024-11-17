"""

using context manager to avoid opening and closing of the db connection multiple times

"""

# from .db_conn import database_connection
# OR
from utils.db_conn import database_connection

books_file = "C:\\Users\\Qanare\\Documents\\ASTROAHAD99\\8_Python\\2_Challenge\\milestone_proj2_V4\\utils\\books.db"
            

def _create_book_table():
    with database_connection(books_file) as cursor:
        # cursor = connection.cursor()
        query = "CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)"
        cursor.execute(query)


def add_book(name, author):
    _create_book_table()

    with database_connection(books_file) as cursor:
        # cursor = connection.cursor()
        query = "INSERT INTO books VALUES(?, ?, 0)" 
        cursor.execute(query, (name, author))


def get_all_books():
    with database_connection(books_file) as cursor:
        query = "SELECT * FROM books"
        cursor.execute(query)
        books_tup = cursor.fetchall() # we will receive list of tuple [(name, author, read), (name, author, read), ...]
        books = [{'name':row[0], 'author':row[1], 'read':row[2]} for row in books_tup]
    return books


def mark_book_as_read(name):
    with database_connection(books_file) as cursor:
        query = "UPDATE books SET read=1 WHERE name=?"
        cursor.execute(query, (name,))


def delete_book(name):
    with database_connection(books_file) as cursor:
        query = "DELETE FROM books WHERE name=?"
        cursor.execute(query,(name,))


