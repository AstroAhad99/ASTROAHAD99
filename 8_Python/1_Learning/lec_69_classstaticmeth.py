
# Now we are going to use @classmethod and @staticmethod decorators
# @classmethod is used when you have to use class level data/attributes 
# for example 
# to modify or use the class level data (variable)
# @classmethod uses cls as first parameter which gives them access
# to the class level data
# @staticmethod on the other hand do not need to use the class level data
# They are function that can do operations within itself.

# When do you classmethod or statismethod
# 1. When you have to interact with class level parameters and valriables
# then you use classmethod decorators
# 2. When you do not have to interact with the class or instance and 
# the functionality of the method can be contained within the method 
# itself then we can use the staticmethod decorators.

# The following is the example for using classmethod used as factory method

class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    @classmethod
    def from_string(cls, book_str):
        title, author, year = book_str.split('-')
        return cls(title, author, int(year))


book_str = "The Great Gatsby-F. Scott Fitzgerald-1925"
new_book = Book.from_string(book_str)
print(new_book.author)


# The following example is using classmethod to handle class level data

class Employee:
    count = 0

    def __init__(self, name):
        self.name = name
        Employee.increment_count()
    
    @classmethod
    def increment_count(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
    

emp1 = Employee('Anne')
emp2 = Employee('Rolf')

print(Employee.get_count())


# The following example is using staticmethod as a utility function

class TemperaturConverter:
    
    @staticmethod
    def celcius_to_fahrenhiet(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celcius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    

print(TemperaturConverter.celcius_to_fahrenhiet(30))
print(TemperaturConverter.fahrenheit_to_celcius(100))

# The following example is using staticmethod as a validation function

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @staticmethod
    def is_valid_email(email):
        return '@' in email
    

print(User.is_valid_email('ahad@gmail.com'))
print(User.is_valid_email('ahmedgmail.com'))