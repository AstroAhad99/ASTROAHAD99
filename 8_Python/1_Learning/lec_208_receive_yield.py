from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))

def get_friend():
    while friends:
        friend = friends.popleft()
        greeting = yield
        print(f"{greeting} {friend}")

def greet(g):
    g.send(None) # Sending none to start the generator is requred
    while True:
        greeting = yield
        g.send(greeting)

greeter = greet(get_friend())
greeter.send(None) # Sending none to start the generator is requred
greeter.send("Hello")

# These are the another set of operations which means that the above code is not blocking
# the below code. This is the power of generators
print("Hello, world!")
print("This is another print statement.")