import time
from threading import Thread

def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f"Hello, {user_input}"
    print(f"Ask user, {time.time() - start}")
    print(greet)

def complex_calculation():
    start = time.time()
    print('Starting calculation...')
    [x**2 for x in range(20000000)]
    print(f'Complex calculation, {time.time() - start}')

start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time() - start}')


thread1 = Thread(target=ask_user)
thread2 = Thread(target=complex_calculation)

start = time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f'Two thread total time: {time.time() - start}')