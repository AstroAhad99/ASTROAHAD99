"""
Filter keeps the list as the generator which means that we can access the next item using the __next__ method
or list method calling.

yield and next keywords should work side by side.

"""
friends = ['Rolf', 'Jose', 'Randy', 'Anna']

def starts_with_r(friend):
    return friend.startswith('R')

friend = filter(starts_with_r, friends)

#print(next(friend))
#print(next(friend))
print(list(friend)) # this will not give error if the list ends


"""
The following is the another way to do the same task using the lambda function
"""

friend = filter(lambda x: x.startswith('R'), friends)
print(list(friend))

"""
The following is the another way to do the same task using the yield keyword
"""

def my_custom_func(func, iterable):
    for i in iterable:
        if func(i):
            yield i
        

genz = my_custom_func(starts_with_r, friends)
print(next(genz))
print(next(genz))