from collections import deque
from types import coroutine

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))

@coroutine
def get_friend():
    while friends:
        friend = friends.popleft()
        greeting = yield
        print(f"{greeting} {friend}")

async def greet(g):
    print("Starting...")
    await g # This is same as: yield from g
    print("Ending...")


greeter = greet(get_friend())
greeter.send(None) # Sending none to start the generator is requred
greeter.send("Hello")
greeter.send("Hello")
# These are the another set of operations which means that the above code is not blocking
# the below code. This is the power of generators
print("Hello, world!")
print("This is another print statement.")