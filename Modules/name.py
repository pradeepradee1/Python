# The Special Variable __name__:

# For Every python program , a special variable __name__ will be added internally.

# This Variable stores information regarding whether the program is executed as an individual program or as a module

# If the program executed as an individual program then the value of this variable is __main__

# If the program executed as an module from some other program then the value of this variable is the name of module 
# where it is defined



print(__name__)


def f1():
    print(__name__)
    if __name__=='__main__' :
        print("The Code executed as a program")
    else:
        print("The Code executed as a module from some other program")


f1()