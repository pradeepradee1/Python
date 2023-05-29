from threading import *
import time

#1) active_count
# This function returns the number of active threads currently running.
print("active count")
'''
def display():
    print(current_thread().getName(),"...started")
    time.sleep(3)
    print(current_thread().getName(),"...ended")

print("The Number of active Threads:",active_count())
t1=Thread(target=display,name="ChildThread1")
t2=Thread(target=display,name="ChildThread2")
t3=Thread(target=display,name="ChildThread3")
t1.start()
t2.start()
t3.start()
print("The Number of active Threads:",active_count())
time.sleep(5)
print("The Number of active Threads:",active_count())
'''

print("Enumerate Functions")
# 2) enumerate
# This function returns a list of all active threads currently running.
'''
import time
def display():
    print(current_thread().getName(),"...started")
    time.sleep(3)
    print(current_thread().getName(),"...ended")
t1=Thread(target=display,name="ChildThread1")
t2=Thread(target=display,name="ChildThread2")
t3=Thread(target=display,name="ChildThread3")
t1.start()
t2.start()
t3.start()
l=enumerate()
print(l)
for t in l:
    print("Thread Name:",t.name)
time.sleep(5)
l=enumerate()
print(l)
for t in l:
    print("Thread Name:",t.name)
'''

print("IsAlive")
'''
def display():
    print(current_thread().getName(),"...started")
    time.sleep(3)
    print(current_thread().getName(),"...ended")
t1=Thread(target=display,name="ChildThread1")
t2=Thread(target=display,name="ChildThread2")
t1.start()
t2.start()
print(t1.name,"is Alive :",t1.is_alive())
print(t2.name,"is Alive :",t2.is_alive())
time.sleep(5)
print(t1.name,"is Alive :",t1.is_alive())
print(t2.name,"is Alive :",t2.is_alive())
'''

#4) Join Method
# If a thread wants to wait until completing some other thread then we should go for join() method.
# t.join(seconds)

print("Join Method")

'''
def display():
    for i in range(10):
        print("Seetha Thread")
        time.sleep(2)
t=Thread(target=display)
t.start()
t.join()#This Line executed by Main Thread
for i in range(10):
    print("Rama Thread")
'''
#Note:
#In the above example Main Thread waited until completing child thread. In this case output is:

print("Join Method")

'''
def display():
    for i in range(10):
        print("Seetha Thread")
        time.sleep(2)
t=Thread(target=display)
t.start()
t.join(5)#This Line executed by Main Thread

for i in range(10):
    print("Rama Thread")
'''
#Note:
#In this case Main Thread waited only 5 seconds.
