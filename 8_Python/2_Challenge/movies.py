# This is the application for adding new movies, list all movies in the database, find a movie by using a title.

# The following are the steps that needs to be followed for completing this task

# 1. Decide where to store the movies (Dictionary is good option)
# 2. What type of data needs to be stored for each movie
# 3. Show the users menu and let the user to pick an option to select
# 4. Implement each requirement (add, list down, find) as a separate function
# 5. Stop running the program when the user type 'q'.

menu = "'a' to add a movie \n'l' to see your movies \n'f' to find a movie by title \n'q' to quit \n Enter your command: "
movies = []


def add_movie(pack):
    movies.append(pack)


def list_down():
    print(movies)


def search(identifier):
    for pack in movies:
        for key, value in pack.items():
            if value == identifier:
                print("The details of the movie are: ", pack)


def main():
    # this is the main function
    print("Welcome to the Application.")
    selection = input(menu)

    while selection != 'q':
        if selection == "a":
            title = input("Enter title of the movie: ")
            director = input("Enter director of the movie: ")
            year = input("Enter year of the movie: ")
            package = {'title':title, 'director':director, 'year':year}
            add_movie(package)
        elif selection == "l":
            list_down()
        elif selection == "f":
            finder = input("Search movie by name, director, or year: ")
            search(finder)
        else:
            print("You have entered an unknown command")
    
        selection = input(menu)


if __name__ == "__main__":
    main()
