"""
The following class shows show we can create our own errors
to extend the capability of error information displaying.
"""

class MyError(TypeError):
    """This error class shows the error message with code"""
    def __init__(self, message, code):
        super().__init__(f"Error code {code}: {message}")
        self.code = code

"""
The following line allows to raise the error message that you have created MyError
"""
#raise MyError('This error occured', 500)

err = MyError('This error occured', 500)
print(err.__doc__) # this function shows the doc which is inside the class
print(err)

