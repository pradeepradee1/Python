#Daemon Thread:
#The threads which are running in the background are called Daemon Threads.
#The main objective of Daemon Threads is to provide support for Non Daemon Threads (like main thread)
#Eg: Garbage Collector

from threading import *
import time

'''
print(current_thread().isDaemon()) #False
print(current_thread().daemon) #False
'''
# current_thread().setDaemon(True)
#RuntimeError: cannot set daemon status of active thread


#Default Nature:
'''
def job():
    print("Child Thread")

t=Thread(target=job)

print(t.isDaemon())#False
t.setDaemon(True)
print(t.isDaemon())#True
'''



#Note: Main Thread is always Non-Daemon and we cannot change its Daemon Nature

#Whenever the last Non-Daemon Thread (Main Thread) terminates automatically all Daemon Threads will be
#terminated.


def job():
    for i in range(10):
        print("Lazy Thread")
        time.sleep(2)

t=Thread(target=job)
# t.setDaemon(True)
t.start()
time.sleep(5)
print("End Of Main Thread")
