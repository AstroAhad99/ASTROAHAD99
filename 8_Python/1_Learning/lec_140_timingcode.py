import time

def timecalculator(func):
    start = time.time()
    func()
    end = time.time()
    print(f"Time to run function: {end - start}")

def powerof(limit):
    return [x**2 for x in range(limit)]

timecalculator(lambda: powerof(500000))


# There is another import function called timeit
# This function takes a string input and that string is the function that is run

import timeit

print(timeit.timeit("[x**2 for x in range(10)]"))
print(timeit.timeit("list(map(lambda x: x**2, range(10)))"))