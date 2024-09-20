# Collatz challenge is famous unsolved mathematical problem in mathematics. 
# The challenge is to start with any positive integer and finally ends with number 1
# You start with any positive integer for example below is 27 and then you check the condition
# If number is even then divide it by 2
# If number is odd then multiply by 3 and add 1 
# Again the check the condition
# You can also count number of steps for each of your iteration to see in how many steps you reach to number 1

number = 27
steps = 0

for i in range(200):
    if number == 1:
        break
    elif number % 2 == 0:
        number = number / 2
        steps = steps + 1
    else:
        number = 3*number + 1
        steps = steps + 1
    
if number == 1:
    print("It took", steps, "steps")
else:
    print("The number didn't reach 1 yet")