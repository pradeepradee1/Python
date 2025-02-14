#Multi Tasking
#Executing several tasks simultaneously is the concept of multitasking.

#There are 2 types of Multi Tasking
#1. Process based Multi Tasking (Multi Processing)
#2. Thread based Multi Tasking (Multi Threading)

#1. Multi Processing:
#1.1) Executing several tasks simmultaneously 
#1.2) where each task is a seperate and independent process is called process based multi tasking
#1.3) multiprocessing implements parallelism.

#2. Multi Threading:
#1.1) Executing several tasks simultaneously 
#1.2) where each task is a seperate and independent part of the same program, is called 
# Thread based multi tasking and each independent part is called a Thread.
#1.3) multithreading implements concurrency.

import threading
import multiprocessing
print("Current Executing Thread:",threading.current_thread().getName())
print(multiprocessing.current_process().name)



# Difference Between MultiThread And MultiProcessing ?

# Multi Thread
# Create Multiple Thread inside a process
# Multi Thread will share memory space and Each one Has specfic instructions and specfic task
# It gloably to connect with another thread

# Multi Process
# Create Multiple Thread inside a process
# Multi Process has own memory space and Each one has its Interprocessor Communication Techniques (e.g., pipes, sockets)
# By using this technique each process share its data , memory 



# For Example :
# I am Running the Chrome and youtube and VisulStudioCode applications in my machine This is Multi Tasking
# All the Different Programs are Different Process 
# We Can See In The Task Manager in windows

# What is Multiple Thread ?
# Multiple Thread live within same Process

# What is Multiple Process ?
# Process Has its own virtual memory Or Address Space
# It Can Create Multiple Thread inside it




#Key Difference
#Thread Are Light Weight
#Process are Heavy Weight

#Note
#The Benifit of multiprocessing is that  error or Memory leak in process won't hurt another process
