from threading import *
import time

#Without multi threading:
print("Without Multithreading")
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print("Double:",2*n)

def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print("Square:",n*n)

numbers=[1,2,3,4,5,6]
begintime=time.time()
doubles(numbers)
squares(numbers)
print("The total time taken:",time.time()-begintime)


#With multithreading:
print("With Multithreading")
from threading import *
import time
def doubles(numbers):
    for n in numbers:
        time.sleep(5)
        print("Double:",2*n)
def squares(numbers):   
    for n in numbers:
        time.sleep(5)
        print("Square:",n*n)


numbers=[1,2,3,4,5,6]
begintime=time.time()
t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=squares,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
#Here Join is waiting for child thread completion
print("The total time taken:",time.time()-begintime)

