from user import User
from saveable import Saveable

class Admin(User, Saveable):
    def __init__(self, username, password, access):
        super(Admin, self).__init__(username, password)
        self.access = access

    def __repr__(self):
        return f'<Admin {self.username}, access {self.access}>'
    
    def to_dict(self):
        return {
            'username' : self.username,
            'password' : self.password,
            'access' : self.access
        }

    """
    Now if we want to insert the Admin user to the database so we will call the function from the
    database.py
    """

    # def save(self):
    #     Database.insert(self.to_dict())

    """
    So self.save will be searched in Admin then in User and then in Saveable

    similarly to_dict() will be found in Admin class

    """