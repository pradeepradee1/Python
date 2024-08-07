#Multi Tasking
#Executing several tasks simultaneously is the concept of multitasking.

#There are 2 types of Multi Tasking
#1. Process based Multi Tasking (Multi Processing)
#2. Thread based Multi Tasking (Multi Threading)

#1. Process based Multi Tasking:
#1.1) Executing several tasks simmultaneously 
#1.2) where each task is a seperate and independent process is called process based multi tasking
#1.3) multiprocessing implements parallelism.

#2. Thread based MultiTasking:
#1.1) Executing several tasks simultaneously 
#1.2) where each task is a seperate and independent part of the same program, is called 
# Thread based multi tasking and each independent part is called a Thread.
#1.3) multithreading implements concurrency.

import threading
import multiprocessing
print("Current Executing Thread:",threading.current_thread().getName())
print(multiprocessing.current_process().name)
