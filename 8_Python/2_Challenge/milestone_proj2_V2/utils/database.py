"""

Concerned with storing and retrieving books from a csv file.

The format of the csv file will be:
name,author,read

sometime if there is no book.txt file exist then it can show error and to avoid this we can create a file simply

"""

books_file = "C:\\Users\\Qanare\\Documents\\ASTROAHAD99\\8_Python\\2_Challenge\\milestone_proj2_V2\\utils\\books.txt"


def _creat_book_table():
    with open(books_file, 'w'):
        pass


def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write(f"{name},{author},False\n")


def get_all_books():
    with open(books_file, 'r') as file:
        # lines = []
        # for line in file.readlines():
        #     lines.append(line.strip().split(','))
        lines = [line.strip().split(',') for line in file.readlines()] # list comprehension 1
        diction = [{"name":line[0], "author":line[1], "read":line[2]} for line in lines] # list comprehension 2
        return diction


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book["name"] == name:
            book["read"] = True

    _save_all_books(books)
    # with open(books_file, 'w') as file:
    #     for book in books:
    #         file.write(f"{book['name']},{book['author']},{book['read']}\n")
    # OR we should create a private function which will be called within this function


def _save_all_books(books): # _ defines that this function must be used internally and not to be called outside.
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n") 


def delete_book(name):
    books_read = get_all_books()
    books = [{"name": book["name"], "author": book["author"], "read": book["read"]} for book in books_read if book["name"] != name]
    _save_all_books(books)