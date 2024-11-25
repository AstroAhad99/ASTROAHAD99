"""
Mutable data is the data which can be changed

and

Immutable is the data which cannot be changed

"""


friends_last_seen = {
    'Rolf':31,
    'Jen':1,
    'Anne':7
}

print(id(friends_last_seen)) # prints the address of the object saved in the RAM location

friends_last_seen = {
    'Rolf':31,
    'Jen':1,
    'Anne':7
}

print(id(friends_last_seen))

friends_last_seen['Rolf'] = 0 # friends_last_seen.__setitem__(self, 'Rolf')

print(id(friends_last_seen)) # Now we have changed the same dictionary so the address will remain the same

my_int = 5
print(id(my_int))

my_int += 1
print(id(my_int)) # when you update this it will create new object


