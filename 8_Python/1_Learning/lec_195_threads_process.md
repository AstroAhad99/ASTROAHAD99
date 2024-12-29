1. Threads are the some sort of the calculations that run on the the CPU core.
2. A process is a wraper around the a thread and the which runs on the core.
3. The purpose of the thread is just to reduce the waiting time.
4. For example: For a single thread: The program as the user for an input and ask to enter the values or something else then once the user has entered all the values then the calculation starts.
5. In multi-threading the resource GIL (global interpreter locator) is released by thread 1 after asking the user for the input. Then this GIL is occupied by the another thread for doing other tasks such as the initial calculation while user is entering the values for the input.
6. In this way the operation time is reduced by using multi-threading. 
7. There is another concept of multi-processing
8. In multi-processing we import a library called multiprocess.

---------------------------------------------

From CHATGPT we have the following information regarding Threading and multiprocessing

1. Threading
    - Threads are the smallest unit in the process which means it is part of the process within same meory space.
    - Comapred to process, threads are lightweight because they share small memory size.
    - They are used to achieve concurrency but due to the GIL in python which is the Global Intrepreter Lock, true parallelism is not achieved using threading.
    - They are useful in I/O bound operations.

2. Multiprocessing
    - Multiprocessing creates separate processes with its own memory space.
    - Processes do not share memory so they can achieve true parallelism as each process has its own python interpreter and GIL
    - They are not useful in I/O bound operations.
    - They are useful in numerical computation or data analysis.
    - Interprocess communications can be done using multiprocessing.Queue or multiprocessing.Pipe

