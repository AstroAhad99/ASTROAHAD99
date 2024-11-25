"""
- counter
- defaultdict

"""


from collections import Counter, defaultdict, OrderedDict

device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]
temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.5])

# Now we are going to see defaultdict
# Default dict never raise key error

coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), 
             ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

"""now we have to create a dictionary from this as"""

{
    'Rolf':['MIT', 'Cambridge'],
    'Jen':['Oxford'],
    'Charlie':['Manchester']
}

# Initailizing the empty dictionary

my_dict = {}

for coworker in coworkers:
    if coworker[0] not in my_dict:
        my_dict[coworker[0]] = [] # adding the default list as value to the key
    my_dict[coworker[0]].append(coworker[1])

print(my_dict)

# Instead of initializing the empty list we can create defaultdict(list)

my_new_dict = defaultdict(list)
#my_new_dict.default_factory = None # Not to initailize here

for coworker, place in coworkers:
    my_new_dict[coworker].append(place)
"   ------list-----------."

#my_new_dict.default_factory = None
my_new_dict.default_factory = int

print(my_new_dict)
print(my_new_dict['Rolf'])
print(my_new_dict['Anne']) # do not exist


"""
The following is the another example of how an we use 
defaultdict when we try to access the key which do not 
exist and the defaultdict will return a pre-configured 
value. The default dict can take input as a function so we
can either pass a list or a lambda function. 
"""

my_company = 'Teclado'

coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Apple Inc.'), ('Anne', 'Google')]

coworker_companies = defaultdict(lambda : my_company)

for people, company in other_coworkers:
    coworker_companies[people] = company


print(coworker_companies[coworker[0]])
print(coworker_companies['Rolf'])