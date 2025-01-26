from functools import wraps

user = {'username':'jose123', 'access_level':'admin'}

def user_has_permission(func):
    @wraps(func)
    def secure_func(panel):
        if user.get('access_level') == 'admin':
            return func(panel)
        else:
            raise RuntimeError
    return secure_func


# The @user_has_permission means that it will run the 
# user_has_permission function first followed by the my_function()

@user_has_permission
def my_function(panel):
    """
    Doc for the my_function function
    """
    return f'Password for {panel} panel is 1234'

print(my_function('movies')) # This will show the details
