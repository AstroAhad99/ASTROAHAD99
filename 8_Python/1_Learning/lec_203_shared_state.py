import time
import random
from threading import Thread

counter = 0

def increment_counter():
    time.sleep(random.random())
    global counter
    time.sleep(random.random())
    counter += 1
    print(f'New counter value: {counter}')
    time.sleep(random.random())
    print("------------------")

if __name__ == '__main__':
    for x in range(10):
        time.sleep(random.random())
        t = Thread(target=increment_counter)
        time.sleep(random.random())
        t.start()
        