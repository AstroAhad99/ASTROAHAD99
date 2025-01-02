def counter(n):
    while n > 0:
        yield(n)
        n -= 1

tasks = [counter(10), counter(20), counter(6)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        print(next(task))
        tasks.append(task)
    except StopIteration:
        print("Task complete")

