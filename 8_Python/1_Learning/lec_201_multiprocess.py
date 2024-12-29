import time
from multiprocessing import Process

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



if __name__ == '__main__':


    # This is a single thread
    start = time.time()
    ask_user()
    complex_calculation()
    print(f'Single thread total time: {time.time() - start}')


    # This is two process
    process1 = Process(target=complex_calculation)
    process2 = Process(target=complex_calculation)
    process1.start()
    process2.start()

    start = time.time()

    process1.join()
    process2.join()

    print(f'Two process total time: {time.time() - start}')

