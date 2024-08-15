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

friends = [("Rolf", 25), ("Anne", 23), ("Charlie", 31)]

for name, age in friends:
    print(f"{name} is {age} years old.")