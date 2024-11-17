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

import json

books_file = "C:\\Users\\Qanare\\Documents\\ASTROAHAD99\\8_Python\\2_Challenge\\milestone_proj2_V3\\utils\\books.json"
            

def _creat_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file)


def add_book(name, author):
    books = get_all_books()
    books.append({'name':name, 'author':author, 'read':False})
    _save_all_books(books)


def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)


def _save_all_books(books): # _ defines that this function must be used internally and not to be called outside.
    with open(books_file, 'w') as file:
        json.dump(books, file)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book["name"] == name:
            book["read"] = True

    _save_all_books(books)


def delete_book(name):
    books_read = get_all_books()
    books = [{"name": book["name"], "author": book["author"], "read": book["read"]} for book in books_read if book["name"] != name]
    _save_all_books(books)