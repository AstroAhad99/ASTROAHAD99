friends_last_seen = {
    'Rolf':31,
    'Jen':1,
    'Anne':7
}


def see_friend(friend, name):
    print(friend is friends_last_seen) # check if the id is same or not
    print(id(friend)) # here you are checking the id of the dictionary
    friend[name] = 0


print(id(friends_last_seen)) # here you are checking the id of the dictionary
print(id(friends_last_seen['Rolf'])) # here you are checking the id of the integer
see_friend(friends_last_seen, 'Rolf')
print(id(friends_last_seen['Rolf'])) # here you are checking the id of the integer
print(id(friends_last_seen)) # here you are checking the id of the dictionary


"""
var.__iadd__() 
this function does not create another variable but make the changes
in the existing variable

whereas var.__add__() 
this function creates another variable and make changes in it.

an example is below

"""

primes = [2, 3, 4]
print(id(primes))
primes += [7, 11]
print(id(primes))
