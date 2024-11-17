"""

Concerned with storing and retrieving books from a csv file.

The format of the csv file will be:
name,author,read

sometime if there is no book.txt file exist then it can show error and to avoid this we can create a file simply

json format

[
    {
        "name":"Code  Clean",
        "author":"Robert",
        "read":True
    }

]


"""

import _sqlite3

books_file = "C:\\Users\\Qanare\\Documents\\ASTROAHAD99\\8_Python\\2_Challenge\\milestone_proj2_V4\\utils\\books.db"
            

def _create_book_table():
    connection = _sqlite3.connect(books_file)
    cursor = connection.cursor()

    query = "CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)"
    cursor.execute(query)

    connection.commit()
    connection.close()

def add_book(name, author):
    _create_book_table()
    connection = _sqlite3.connect(books_file)
    cursor = connection.cursor()

    #query = "INSERT INTO books VALUES('{name}', '{value}', 0)"
    #cursor.execute(query)
    query = "INSERT INTO books VALUES(?, ?, 0)" # to avoid sql injection attack
    cursor.execute(query, (name, author)) # to avoid sql injection attack

    connection.commit()
    connection.close()


def get_all_books():
    connection = _sqlite3.connect(books_file)
    cursor = connection.cursor()

    query = "SELECT * FROM books"
    cursor.execute(query)
    books_tup = cursor.fetchall() # we will receive list of tuple [(name, author, read), (name, author, read), ...]
    books = [{'name':row[0], 'author':row[1], 'read':row[2]} for row in books_tup]
    connection.close() #there is anything to commit
    return books


def mark_book_as_read(name):
    connection = _sqlite3.connect(books_file)
    cursor = connection.cursor()

    query = "UPDATE books SET read=1 WHERE name=?"
    cursor.execute(query, (name,))

    connection.commit()
    connection.close()


def delete_book(name):
    connection = _sqlite3.connect(books_file)
    cursor = connection.cursor()

    query = "DELETE FROM books WHERE name=?"
    cursor.execute(query,(name,))

    connection.commit()
    connection.close()


