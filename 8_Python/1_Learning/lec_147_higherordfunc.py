"""This is an example of calling a function into another function"""

def greet():
    print("Hello")


def before_and_after(func):
    print("before")
    func()
    print("after")

before_and_after(lambda: 5)
before_and_after(greet)

"""Next here we are going to build a search function that can search a dictionary by any key that we
take as an input argument from the user"""


movies =[ {'name':'The Matrix', 'director':'Ahad'},
          {'name':'A beautiful day', 'director':'Ali'},
          {'name':'The Irishman', 'director':'Ahmed'},
          {'name':'Klaus', 'director':'Adil'},
          {'name':'1917', 'director':'Aamir'}
]

search_by = input("Search by name or director?: ")
looking_for = input("You are looking for?: ")


def find_movie(expected, finder) ->str:
    for movie in movies:
        if finder(movie) == expected:
            print(movie)


find_movie(looking_for, lambda movie: movie[search_by])

"""
So this lambda function is passed inside this function which is called (find_movie)
then we do iteration to find the value from the key which is added like (name or director)
and it checks to match with the (looking_for) value. Finally if it finds the value then it matches 
that and returns the movie dictionary

"""