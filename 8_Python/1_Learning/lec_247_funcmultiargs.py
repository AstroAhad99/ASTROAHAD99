def add_all(*args): #any number of argument
    return sum(args)

def pretty_print(**kwargs): #any number of named arguments
    result = []
    for k, v in kwargs.items():
        result.append(f"For {k} we have {v}.")
    return "\n".join(result)

print(add_all(1, 2, 3, 4, 5))

# Using print for the result of pretty_print
print(pretty_print(username="ahad99", access_level="admin"))

# Passing a dictionary with **kwargs unpacking
print(pretty_print(**{'username': 'ahad99', 'access_level': 'admin'}))
