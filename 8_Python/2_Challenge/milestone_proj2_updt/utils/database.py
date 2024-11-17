"""

Concerned with storing and retrieving books from a list.

"""

books = []


def add_book(name, author):
    books.append({"name":name, "author":author, "read":False})


def get_all_books():
    return books


def mark_book_as_read(name):
    for book in books:
        if book["name"] == name:
            book["read"] = True
            return


def delete_book(name):
    # for book in books:
    #     if book['name'] == name:
    #         books.pop(book)

    # The following line is giving error because of the scope of the variable book so we will
    # books = [{"name":book["name"], "author":book["author"], "read":book["read"]} for book in books: if book["name"]!=name]

    global books
    books = [{"name": book["name"], "author": book["author"], "read": book["read"]} for book in books if book["name"] != name]
