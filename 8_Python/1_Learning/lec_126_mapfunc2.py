class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


users = [
    {'username':'ahad', 'password':'123'},
    {'username':'ali', 'password':'456'}
]

"""
The the class method has the property that it can be called from the outside
"""
genz = [User(**data) for data in users] #dictionary unpacking
user1 = genz[0]
print(user1.username)
print(user1.password)

"""Using Map function"""

#genz = map(User.from_dict, users)
#user1 = next(genz)
#print(user1.username, user1.password)
#user2 = next(genz)
#print(user2.username, user2.password)