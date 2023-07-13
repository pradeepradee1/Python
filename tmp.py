# import os,sys
# try:
#     print("try")
#     os._exit(0)
# except NameError:
#     print("except")
# finally:
#     print("finally")


a=[3,2,2,3]
#a.remove(3)
for i in range(0,a.count(3)):
    a.remove(3)
    a.append("_")
print(a)

