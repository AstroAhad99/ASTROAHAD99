"""
Generator is a function that gives that is has saved in the last function call. It does not saves everything
but only the last value of that call. It remembers the last value.

"""

# def hundred_numbers():
#     nums = []
#     i = 0
#     while i < 100:
#         yield i
#         i += 1

# g= hundred_numbers()
# print(next(g))
# print(next(g))
# print(list(g))


def prime_generator(bound):

    for n in range(2,bound):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            yield n

g= prime_generator(10)
print(next(g))
print(next(g))
print(list(g))
