from random import *

#1) random()
# random = between 0 and 1 (not inclusive)

for i in range(5):
    print(random())

#2) randint()
# randint = between x and y ( inclusive)

for i in range(5):
    print(randint(1,5))

#3) uniform()
# uniform(x,y) = in between x and y ( not inclusive)
for i in range(5):
    print(uniform(1,10))

#4) randrange()
for i in range(5):
    print(randrange(5))

#5) choice()
list=["Sunny","Bunny","Chinny","Vinny","pinny"]
for i in range(5):
    print(choice(list))


