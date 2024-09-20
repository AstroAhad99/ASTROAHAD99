### Python Udemy Course 

#### Section 1: Basics

1. Writing the variable name in all capital letters means that values of these variables are not intended to change.

2. // using double division sign removes the decimal point in the calculation.

2. % sign is used for calculating the remainger of division operation like this. 
```
cal = 13 % 5
print(cal)

result -> 3

```

3. Adding a backslash in the front of the characters is used to remove the meaning of the character.

4. Multiline string can be added by adding """ tripple qoutes like this """. It can also be used as comments instead of # key. 

5. In python we can also use f strings like this.

``` 
age = 34
print(f"You are {age}") 

 ```
6. Another way of doing the same thing is to use format keyword. An example for this is given as:
```
name = "ahad"
ahad_greetings = "How are you {}"
final_greetings = ahad_greetings.format(name)
print(final_greeting)

OR

user = "ahad"
ahad_greetings = "How are you {name}"
final_greetings = ahad_greetings.format(name=user)
print(final_greeting)

OR

name = "ahad"
ahad_greetings = "How are you {}"
print(ahad_greetings.format(name))


```

7. The truth table is used for AND and OR keyword

8. ```print(True and 18)``` returns 18
```print(True or 18)``` return True

9. AND Logic is 
```
Start -> If First value is True -> Return 2nd Value -> Else return 1st Value

```

10. OR Logic is 

```
Start -> If First value is True -> Return 1st Value -> Else return 2nd Value

```

11. We can't append to a tupple

12. What we can do is like
```

friends = ("Ahad", "Ali")
friends = friends + ("Ahmed",)

```

13. Sets does not contain duplicate items, or ordered items. We can do add/remove operation in sets. We can also do difference command.

14. In sets we can do command like symmetric_difference. This will give us the output which is not common in both.

15. Sets are useful in the cases when you have to perform difference or intersection operation on data so there sets are very userful. Sets are also in curly brackets.

16. Dictionary contains both keys and values.

17. Assignment in dictionary is like this 
```
new_diction["key"] = 12

```

18. A list of tuples can easily converted  dictionary like this
```
friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
friends_age = dict(friends)
print(friends_age)

```

19. Sum and len functions allows to compute the sum of the numbers and len function allows to compute the length of the list.

20. For sum operation list is the best option because it is flexible which means we can add more values.


21. We have studied about if-else statement which is very easy. There is importance of indentation.

22. If moves through bool function like this ```bool(5)```

23. There is also another keyword called (in) which is useful when you are checking a single thing in a list of items.

24. While is also passing from the bool function. 

25. In for loop the 
```
ele = [1, 2, 3, 4, 5]
for index in ele:
    print(index)
```
here the index can be any other variable.

26. Destructing means assigning a tupple to multiple variables


27. Iteration in dictionary is also possible. we can go through both either keys or values like this

```

friends_ages = {"Rolf":25, "Anne":24, "Bob":22}

for friends in friends_ages:
    print(friends)

for friends in friends_ages.values():
    print(friends)

for names, ages in friends_ages.items():
    print(f"{names} is {ages} year old.")

```
28. Break and continue is another important keywords here is the example. Break keyword is used with the for loop to break the iteration loop and comes out. The CONTINUE keyword on the otherhand does not break the loop but instead it skips that particular iteration and continues the program.

29. The for loop can also be used not only to repeat over the number of time but also move over the collection of elements.

30. The FOR or WHILE loop has another unique property called ELSE. If you want to print something or do anything else after the successful complition of the loop you can use the ELSE keyword in the same indentation as the loop. If in the loop you have used break keywork and the loop is breaked during the execution then this ELSE will not be executed.

31. Finding a number if it is prime or not using for loop and else keyword is done in the find_prime_num_loops.py.

32. This does not run anything
```
for n in range(2,2):
    print(n)
```

33. Slicing of a list, tuple is also very useful
```

friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]
print(friends[2:4]) # This will start from 2 and ends at 3
print(friends[1:]) # Skips element at index 0
print(friends[:4]) # Skips element at index 4
print(friends[:]) # Gets a new list
print(friends[-3:]) # Jen is at -1 so it will start from Anna
print(friends[:-2]) # Starting from 0 and ends at Anna

```
 
34. List comprehension means if you want to perform some actions (calculation) then you can do inside the list itself like this
```

names = ["Rolf", "Bob", "Jen"]
friend = input("Enter the name of the friend: ")
lower = [name.lower() for name in names]
if friend.lower() in lower:
    print(f"My friend name is {friend.title()}.")

```

35. The same thing we can do for sets and dictionary comprehension

36. There is another function called ZIP which is used to combine two or more list together like in a tuple.

37. Another function is the Enumerate which give the corresponding index of the element in the simple list.
