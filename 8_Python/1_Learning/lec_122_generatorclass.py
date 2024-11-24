"""
Iterators are the functions that iterate over the existing list one by one
using the next() method.

Iterables are the functions that can iterate over the complete list

"""

class FirstHundredGenerator:
    
    def __init__(self):
        self.number = 0

    def __next__(self):
        current = self.number
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()
    
my_gen = FirstHundredGenerator()
print(next(my_gen))
print(next(my_gen)) 