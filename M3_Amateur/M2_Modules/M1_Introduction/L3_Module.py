from L1_Module import product,x
print(x)
print(product(10,20))
#print(add(1,3)) ---> Error add module is not defined

#We can import all members of a module as follows
from L1_Module import *
print(x)
print(product(10,20))
print(add(1,3)) 