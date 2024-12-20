## The Following lines of code is for taking input from the user

# your_name = input("My name is: ")
# print(f"Your name is {your_name}")

## Doing Calculations

# age = int(input("Enter your age: "))
# #age_num = int(age)
# print(f"You have lived {age * 12} months.")

# print(bool(13)) #True
# print(bool(0)) #False
# print(bool("")) #False
# print(bool("Something")) #True

# print(True and 18)

## Lists

# friends = ["Ahad", "Ali", "Ahmed"]
# print(friends[0])

# age_friends = [
#     ["Ahad", 25], 
#     ["Ali", 24]
#     ]

# print(age_friends[0][1])

# age_friends.append(["Ahmed", 26])

# print(age_friends)

## Tupples

# short_tupple = ("Ahad", "Ali")
# print(short_tupple[1])

## Sets

# art_friends = {"Rolf", "Anne", "Jen"}
# science_friends = {"Jen", "Charlie"}

# art_but_not_science = art_friends.difference(science_friends)
# science_but_not_art = science_friends.difference(art_friends)

# print(art_but_not_science)
# print(science_but_not_art)

# not_in_both = art_friends.symmetric_difference(science_friends) #we can do opposite also
# print(not_in_both)

# art_and_science = art_friends.intersection(science_friends)
# print(art_and_science)

## Sets exercise

# nearby_people = {'Rolf', 'Jen', 'Anna'}
# user_friends = set()  # This is an empty set, like {}
# New_Friend = input("Enter the name of the friend: ")
# user_friends.add(New_Friend)

# only_friend = nearby_people.intersection(user_friends)
# print(only_friend)

# grades = [80, 90, 100]

# total = sum(grades)
# length = len(grades)

# average = total/length
# print(average)

## Quick exercise
# players = [{'name':'Ahad', 'numbers':{1, 2, 3, 4, 5}}, {'name':'Ahad', 'numbers':{4, 5, 6, 7, 8}}]
 
# common_num =  players[0]['numbers'].intersection(players[1]['numbers'])
# final_string = "Player {} got {} numbers right"
# print(final_string.format(players[0]['name'], len(common_num)))


# friends = ["Rolf", "Anne", "Charlie"]
# comma_separated = ", ".join(friends)
# print(f"My friends are {comma_separated}.")

## if-else-elif-in

# friends = ["Rolf", "Anne", "Bob"]
# user_name = input("Enter user name: ")
# if user_name in friends:
#     print(f"Hello, {user_name}")
# else:
#     print("I dont know you")

#is_learning = True
# while is_learning:
#     print("You are learning!")
#     user = input("Are you still learning? ")
#     if user != "yes":
#         is_learning = False

## Practice
# ask = input("What do you want to do? ")
# check = True
# while check:
#     if ask == 'p':
#         print("Hello")
#         ask = input("Type again: ")
#     elif ask == 'q':
#         check = False
#     else:
#         ask = input("Type again: ")

## Another way of doing the same thing
# user_input = input("Enter the input p or q: ")

# while user_input != 'q':
#     if user_input == 'p':
#         print("Hello")
#     user_input = input("Enter again: ")

# ## For loop good example
# students = [
# {"name":"Rolf", "grade":90},
# {"name":"Rob", "grade":78},
# {"name":"Jen", "grade":100},
# {"name":"Anne", "grade":80}
# ]

# for student in students:
#     name = student["name"]
#     grade = student["grade"]

#     print(f"{name} has a grade of {grade}")

## Destructuring

# friends = [("Rolf", 25), ("Anne", 23), ("Charlie", 31)]

# for name, age in friends:
#     print(f"{name} is {age} years old.")

## Iterating into dictionaries

# friends_ages = {"Rolf":25, "Anne":24, "Bob":22}

# for friends in friends_ages:
#     print(friends)

# for friends in friends_ages.values():
#     print(friends)

# for names, ages in friends_ages.items():
#     print(f"{names} is {ages} year old.")

## Using break and continue keywords

# cars = ['ok', 'ok', 'ok', 'faulty', 'ok', 'ok']

# for status in cars:
#     if status == 'faulty':
#         print("This car is faulty. Breaking the loop")
#         break
#     print(f"This car is {status}")

# cars = ['ok', 'ok', 'ok', 'faulty', 'ok', 'ok']

# for status in cars:
#     if status == 'faulty':
#         #print("This car is faulty. Breaking the loop")
#         continue
#     print(f"This car is {status}")

## Challging Code Task

# for num in range(1, 101, 1):
#     if num % 3 == 0:
#         if num % 5 == 0:
#             print("FizzBuzz")
#         else:
#             print("Fizz")
#     elif num % 5 == 0:
#         if num % 3 == 0:
#             print("FizzBuzz")
#         else:
#             print("Buzz")
#     else:
#         print(num)

## List Slicing

# friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]
# print(friends[2:4]) # This will start from 2 and ends at 3
# print(friends[1:]) # Skips element at index 0
# print(friends[:4]) # Skips element at index 4
# print(friends[:]) # Gets a new list
# print(friends[-3:]) # Jen is at -1 so it will start from Anna
# print(friends[:-2]) # Starting from 0 and ends at Anna

## List Comprehension
## This is normal way
# numbers = [0, 1, 2, 3, 4]
# double_numbers = []

# for number in numbers:
#     double_numbers.append(number * 2)

# print(double_numbers)

## List comp way

# double_numbers = []

# double_numbers = [number * 2 for number in numbers]
# print(double_numbers)


# double_numbers = []

# double_numbers = [number * 2 for number in range(5)]
# print(double_numbers)

# friend_ages = [22, 23, 24, 25]

# outputs = [f"My friend is {age} years old." for age in friend_ages]
# print(outputs)

# names = ["Rolf", "Bob", "Jen"]
# friend = input("Enter the name of the friend: ")
# lower = [name.lower() for name in names]
# if friend.lower() in lower:
#     print(f"My friend name is {friend.title()}.")

## List Comprehensions with conditionals

# ages = [22, 21, 33, 43, 11]

# odds = [age for age in ages if age % 2 == 0]
# print(odds)

# friends = ["Rolf", "ruth", "Charlie", "Jen"]
# guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

# friends_lower = set([friend.lower() for friend in friends])
# guests_lower = set([guest.lower() for guest in guests])

# print(friends_lower.intersection(guests_lower))

## Doing the same thing but using list comprehensions

# friends = ["Rolf", "ruth", "Charlie", "Jen"]
# guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

# guests_lower = [g.lower() for g in guests]
# present_friends = [common.title() for common in friends if common.lower() in guests_lower]

# print(present_friends)

## Sets and dictionary comprehension
# Sets comprehension
# friends = ["Rolf", "ruth", "Charlie", "Jen"]
# guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

# friends_lower = {f.lower() for f in friends}
# guests_lower = {g.lower() for g in friends}

# present_friends = friends_lower.intersection(guests_lower)

# present_friends = {name.title() for name in present_friends}
# print(present_friends)

## Dictionary Comprehension
# friends = ["Rolf", "Bob", "Jen", "Anne"]
# time_seen = [3 , 5, 7, 9]

# name_time = {friends[i] : time_seen[i] for i in range(len(friends)) if time_seen[i]>5}
# print(name_time)

#________________________________________

## ZIP function

# friends = ["Rolf", "Bob", "Jen", "Anne"]
# time_seen = [3 , 5, 7, 9]

# combined = dict(zip(friends, time_seen))
# print(combined)

#________________________________________

## Enumerate Function
# friends = ["Rolf", "Bob", "Jen", "Anne"]

# for counter, friend in enumerate(friends, start = 1):
#     print(counter, friend)

# for counter, friend in enumerate(friends):
#     print(counter, friend)

# print(dict(enumerate(friends))) # Build dictionary
# print(list(enumerate(friends))) # Build tuple

#________________________________________

# #Print position of the character found in the string

# str1 = "Is it going well?" 
# str2 = "go"
# print(str1.find(str2))

# # If it doesnt finds anything then it will return -1
# # find command is case sensitive
# # This will return the first occurance of the str2 in str1
# str1 = "Hi hey hello he." 
# str2 = "he"
# print(str1.find(str2))

#________________________________________

# #Substings

# #In substring the first index is the index of the letter and the last index letter is not 
# #added in it

# sentence = "I like rocks but they seem indifferent."
# conjunction_index = sentence.find("but")
# left_side = sentence[0:conjunction_index] 
# #left_side = sentence[0:conjunction_index-1] 
# right_side = sentence[conjunction_index + 3:]
# #right_side = sentence[conjunction_index + 4:]
# classy_sentence = left_side + "yet" + right_side
# print(classy_sentence)

#________________________________________

# # Creating a simple function
# def greet():
#     name = input("Enter your name: ")
#     print(f"Hello, {name}!")

# greet()

#________________________________________


# # Creating function with arguments

# # The following is the list of dictionary

# cars = [{"make":"Ford", "model":"Fiesta","mileage":23000, "fuel_consumption":460},
#        {"make":"Ford", "model":"Focus","mileage":17000, "fuel_consumption":350},
#        {"make":"Mazda", "model":"MX-5","mileage":49000, "fuel_consumption":900},
#        {"make":"Mini", "model":"Cooper","mileage":31000, "fuel_consumption":235}
#        ]

# def calculate_mpg(car):
#     mpg = car["mileage"] / car["fuel_consumption"]
#     name = f"{car["make"]} {car["model"]}"
#     print(f"{name} does {mpg} miles per gallon.")

# for car in cars:
#     calculate_mpg(car)


#__________________________________________

# # Now we are going to call functions inside funtions


# cars = [{"make":"Ford", "model":"Fiesta","mileage":23000, "fuel_consumption":460},
#        {"make":"Ford", "model":"Focus","mileage":17000, "fuel_consumption":350},
#        {"make":"Mazda", "model":"MX-5","mileage":49000, "fuel_consumption":900},
#        {"make":"Mini", "model":"Cooper","mileage":31000, "fuel_consumption":235}
#        ]

# def calculate_mpg(car_mileage, car_consump):
#     mpg = car_mileage / car_consump
#     return mpg


# def car_name(car): 
#     name = f"{car["make"]} {car["model"]}"
#     return name


# def print_car_info(car):
#     mpg = calculate_mpg(car['mileage'], car['fuel_consumption'])
#     name = car_name(car)
#     return f"{name} does {mpg} miles per gallon."

# for car in cars:
# #   print(car['mileage'])
#     print(print_car_info(car))

#__________________________________________

# # The folowing is we are going to define the function with named arguments.
# # You can add a default value also in the add function
# # You can also define the values in the function when calling them after defining the function


# def add(x=2, y=1):
#     total = x + y
#     print(total)

# print(add(5, 5))

# print(1, 2, 3, 4, 5, sep="-")

#__________________________________________

# # Now we are going to do the lambda function that we can use instead 
# # of defining function. Lambda is use as one liner function.

# # def average(sequence):
# #     return sum(sequence)/len(sequence)

# average = lambda sequence: sum(sequence)/len(sequence)

# students = [{"name":"Rolf", "grade":(67, 90, 95, 100)},
#             {"name":"Bob", "grade":(56, 78, 80, 90)},
#             {"name":"Jen", "grade":(98, 90, 95, 99)},
#             {"name":"Anne", "grade":(100, 100, 95, 100)}]


# for student in students:
#     print(average(student["grade"]))


# Creating functions using lambda inside the dictionary

# operations = {"avg":lambda seq: sum(seq)/len(seq),
#               "sum":lambda seq: sum(seq),
#               "max":lambda seq: max(seq)}

# students = [{"name":"Rolf", "grade":(67, 90, 95, 100)},
#              {"name":"Bob", "grade":(56, 78, 80, 90)},
#              {"name":"Jen", "grade":(98, 90, 95, 99)},
#              {"name":"Anne", "grade":(100, 100, 95, 100)}]


# for student in students:
    
#     name = student["name"]
#     grade = student["grade"]

#     print(f"Student name is: {name}")
#     action = input("Enter the operation name (avg), (sum), (max): ")

#     set_function = operations[action]
#     print(set_function(grade))

# _______________________________________________________

# def over_age(data, getter):
#     return getter(data) >= 18
 
# user = { 'username': 'rolf123', 'age': '35' }
 
# print(over_age(user, lambda x: int(x['age'])))

# _______________________________________________________

# movies = [{'title': 'aa', 'director': 'sdf', 'year': '123'}, {'title': 'qer', 'director': '345', 'year': 'gfd'}]

# inp = str(input("Something: "))

# for dicti in movies:
#     print(dicti)
#     for key, value in dicti.items():
#         if value == inp:
#             print("Found")
#             break

# _______________________________________________________


for i in range(2, 10):
    print(i)