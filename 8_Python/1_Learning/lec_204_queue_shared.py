import threading
import queue

# Shared variable and lock
counter = 0
counter_lock = threading.Lock()

def worker(task_queue):
    global counter
    while not task_queue.empty():
        task = task_queue.get()  # Get a task from the queue
        
        # Safely increment the counter
        with counter_lock:
            counter += 1
            print(f"Thread {threading.current_thread().name} incremented counter to {counter}")
        
        task_queue.task_done()  # Mark the task as done


if __name__ == "__main__":

    # Create a queue and populate it with tasks
    task_queue = queue.Queue()
    num_tasks = 10  # Number of tasks
    for i in range(num_tasks):
        task_queue.put(f"Task {i + 1}")

    # Create threads
    threads = []
    for i in range(10):  # 3 threads
        thread = threading.Thread(target=worker, args=(task_queue,), name=f"Thread-{i+1}")
        threads.append(thread)

    # Start threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Ensure all tasks are completed
    task_queue.join()

    print(f"Final counter value: {counter}")
