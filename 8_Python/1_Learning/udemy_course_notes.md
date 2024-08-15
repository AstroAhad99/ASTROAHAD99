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

15. Sets are useful in the cases when you have to perform difference or intersection operation on data so there sets are very userful.

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