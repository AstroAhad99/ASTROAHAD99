from functools import wraps

def get_current_user_role() -> int:
    return 0

def access_control(access_level: int):
    def user_has_permission(func):
        @wraps(func)
        def secure_func(*arg, **kwargs):
            if get_current_user_role() <= access_level:
                return func(*arg, **kwargs)
            else:
                raise PermissionError("You do not have the proper access level.")
        return secure_func
    return user_has_permission
    
@access_control(0)
def delete_file(filename):
    # perform the deletion operation
    print(f'{filename} is deleted!')


print(delete_file("MyFile"))