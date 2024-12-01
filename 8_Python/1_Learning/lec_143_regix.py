"""
Useful for fetching data from the 
"""

import re

email = 'ahad99.shalwani@gmail.com'

expression1 = '[a-z]+' # This fetch all the characters only into list form
matches1 = re.findall(expression1, email)

expression2 = '[a-z\.]+' # This fetch all the characters and also include the .
matches2 = re.findall(expression2, email)

print(matches1)
print(matches2)


# there is another simple way of doing the same

parts = email.split('@')
name = parts[0]
domain = parts[1]

print(name)
print(domain)


price = 'Price: $189.50'
price2 = 'Price: $189,434.589'
expression3 = 'Price: \$(189.50)' # To take out 2 groups then we will use this
expression4 = '189.50' # If we want only the number in the group 0
expression5 = 'Price: \$([0-9,]*\.[0-9])*' #any number or , then . then any number


matches3 = re.search(expression5, price2)
print(matches3.group(0))
print(matches3.group(1))

number = float(matches3.group(1).replace(',',''))
print(number)




def is_filename_safe(filename):
    # Updated regular expression
    regex = r'^[a-zA-Z0-9][a-zA-Z0-9\-_()]*\.(jpg|jpeg|png|gif)$'
    return re.match(regex, filename) is not None


"""

Explanation:
1. ^ ensures the match starts at the beginning of the string.
2. [a-zA-Z0-9] ensures the filename starts with a valid character.
3. [a-zA-Z0-9\-_()]* allows any combination of valid characters (including zero occurrences).
4. \.(jpg|jpeg|png|gif)$ ensures the filename ends with one of the valid extensions.

"""

print(is_filename_safe("image1.jpg"))  # True
print(is_filename_safe("my_image.png"))  # True
print(is_filename_safe("file-name.gif"))  # True
print(is_filename_safe("_not_valid.gif"))  # False
print(is_filename_safe("invalid.txt"))  # False
print(is_filename_safe("12345.jpeg"))  # True
