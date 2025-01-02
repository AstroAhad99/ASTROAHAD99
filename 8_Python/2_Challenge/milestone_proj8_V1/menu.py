from app import books

from logger_config import logger

def print_best_books():
    logger.debug('Finding best books...')
    best_books = sorted(books, key=lambda x: x.rating)[:10]
    for book in best_books:
        print(book)

def print_cheapest_books():
    logger.debug('Finding cheapest books...')
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)

books_generator = (x for x in books)

def next_book():
    # for book in books:
    #     print(book)
    #     user_input = input("Do you wish to see the next book? (y/n)")
    #     if user_input != 'y':
    #         break
    logger.debug('Finding next book...')
    print(next(books_generator))
    

if __name__ == '__main__':
    note = """
    b - best books
    c - cheapest books
    n - next book
    q - quit
    """
    print(note)
    user_input = input("Enter your choice: ")
    while user_input != 'q':
        if user_input == 'b':
            print_best_books()
        elif user_input == 'c':
            print_cheapest_books()
        elif user_input == 'n':
            next_book()
        else:
            print("Invalid input")
        user_input = input("Enter your choice: ")
    print("Goodbye!")
    