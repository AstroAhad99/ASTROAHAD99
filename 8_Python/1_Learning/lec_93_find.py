from lec_92_file_opera import *

def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i
    raise NotFoundError(expected)


class NotFoundError(Exception):
    pass
#    def __init__(self, number, code):
#        super.__init__(f"This number was expected {number}. Error code is {code}.")

print(__name__)