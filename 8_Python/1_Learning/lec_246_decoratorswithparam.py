from functools import wraps

user = {'username':'jose123', 'access_level':'admin'}

def third_level(access_level): # this function has been made for decorators to have input argument
    def user_has_permission(func):
        @wraps(func)
        def secure_func(panel):
            if user.get('access_level') == access_level:
                return func(panel)
            else:
                raise RuntimeError
        return secure_func
    return user_has_permission


# The @user_has_permission means that it will run the 
# user_has_permission function first followed by the my_function()

@third_level("admin")
def my_function(panel):
    """
    Doc for the my_function function
    """
    return f'Password for {panel} panel is 1234'

print(my_function('movies')) # This will show the details
