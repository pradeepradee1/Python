#Setting and Getting Name of a Thread
from threading import *
print(current_thread().getName())
current_thread().setName("Pawan Kalyan")
print(current_thread().getName())
print(current_thread().name)

