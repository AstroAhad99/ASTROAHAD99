"""
If you catch the type error then it will not show the description of the error that you have added in the function
block with the raise exception.

"""

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'Car {self.make} {self.model}'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __repr__(self):
        return f'{self.cars}'

    def add_cars(self, car):
        #print('This method is a work in progress')
        #raise NotImplementedError("We can't add cars to the garage yet.")
        if not isinstance(car, Car):
            raise TypeError(f"Tried to add a '{car.__class__.__name__}' to the garage, but you can only add Car objects.")
        self.cars.append(car)



ford = Garage()
car1 = Car('Ford', 'Fiesta')
car2 = Car('Toyota', 'Carrolla')
try:
    ford.add_cars(car1)
    ford.add_cars(car2)
    #ford.add_cars('car')
except TypeError:
    print('Your car was not a car.')
finally:
    print(f'The garage has now {len(ford)} cars.')
    print(ford)