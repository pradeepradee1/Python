
#Multi Tasking
#Executing several tasks simultaneously is the concept of multitasking.

#There are 2 types of Multi Tasking
#1. Process based Multi Tasking (Multi Processing)
#2. Thread based Multi Tasking (Multi Threading)

#1. Process based Multi Tasking:
#Executing several tasks simmultaneously where each task is a seperate and
#independent process is called process based multi tasking

#2. Thread based MultiTasking:
#Executing several tasks simultaneously where each task is a seperate and 
#independent part of the same program, is called Thread based multi tasking 
#and each independent part is called a Thread.


import threading
import multiprocessing
print("Current Executing Thread:",threading.current_thread().getName())
print(multiprocessing.current_process().name)
