user = {'username':'jose123', 'access_level':'admin'}

def user_has_permission(func):
    def secure_func():
        """This is doc for secure_func()"""
        if user.get('access_level') == 'admin':
            return func()
    return secure_func


# The @user_has_permission means that it will run the 
# user_has_permission function first followed by the my_function()

@user_has_permission
def my_function():
    return 'Password for admin panel is 1234'

print(my_function)
print(my_function.__name__) #This will print the name of secure_func name
print(my_function.__doc__) #This will print the name of secure_func doc
