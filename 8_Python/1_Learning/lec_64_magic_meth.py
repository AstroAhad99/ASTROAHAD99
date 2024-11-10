# Everything in python is an object
# Dunder methods are very useful in python as they are used when we 
# are creating classes


#_________________________________

# movies = ['Matrix', 'Finding Nemo']
# print(movies.__class__)

#__________Dunder Methods_________

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self): # code oriented function
        return f'Garage {self.cars}'

    def __str__(self): # more user oriented
        return f'Garage has {len(self)} cars'

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

#print(len(ford.cars))
print(len(ford))

# Now if we have to print the length of the cars without using the variable cars
# then we have to assign a function in class called __len__

# The another dunder method is which can access an item in the list

# print(ford[1]) #getitem def

# for cars in ford:
#     print(cars)

# Using the dunder method for a repr

print(ford)