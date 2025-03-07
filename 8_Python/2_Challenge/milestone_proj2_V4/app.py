from IPython.core.release import author

from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            #pass
            prompt_add_book()
        elif user_input == 'l':
            #pass
            list_books()
        elif user_input == 'r':
            #pass
            prompt_read_book()
        elif user_input == 'd':
            #pass
            prompt_delete_book()
        else:
            print("Unknown user input. Please enter the input again")
        user_input = input(USER_CHOICE)


def prompt_add_book(): #ask for book name and author
    name = input("Enter the name of the new book: ")
    author = input("Enter the new book author: ")
    database.add_book(name, author)


def list_books(): #show all the books in our list
    books = database.get_all_books()
    for book in books:
        read = "Yes" if book["read"] else "No"
        print(f"{book['name']} by {book['author']} is read: {read}")


def prompt_read_book(): #ask for book name and change it to "read" in our list
    name = input("Enter the name of the book you just finished reading: ")
    database.mark_book_as_read(name)


def prompt_delete_book(): #ask for book name and remove book from the list
    name = input("Enter the name of the book you want to delete: ")
    database.delete_book(name)

if __name__ == "__main__":
    menu()
