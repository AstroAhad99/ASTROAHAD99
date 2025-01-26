from functools import wraps

user = {'username':'jose123', 'access_level':'admin'}

def user_has_permission(func):
    @wraps(func)
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
        else:
            raise RuntimeError
    return secure_func


# The @user_has_permission means that it will run the 
# user_has_permission function first followed by the my_function()

@user_has_permission
def my_function():
    """
    Doc for the my_function function
    """
    return 'Password for admin panel is 1234'

print(my_function()) # This will show the details
print(my_function) # This will just return the object 
print(my_function.__name__)
print(my_function.__doc__)
