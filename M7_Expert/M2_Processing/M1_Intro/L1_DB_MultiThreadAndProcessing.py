#Multi Threading And Multi Processing both are ways to achieve MultiTasking.

#For Example :
# I am Running the Chrome and youtube and VisulStudioCode applications in my machine This is Multi Tasking
# All the Different Programs are Different Process 
# We Can See In The Task Manager in windows

#What is Multiple Thread ?
# Multiple Thread live within same Process

#What is Multiple Process ?
# Process Has its own virtual memory Or Address Space
# It Can Create Multiple Thread inside it


#Difference Between MultiThread And MultiProcessing

#Multi Thread will share address space (Virtual Space) , Each Has Its own instructions 
#and specfic task and They will execute its own code and They Have Stack Memory anh Heap Memory 
#Finally Share its address Space beacause of its gloably to access the another thread

#MultiProcess will own address space (Virtual Space) and each has its Interprocessor Communocation Techniques 
#by using this technique each process share its data , memory 

#Key Difference
#Thread Are Light Weight
#Process are Heavy Weight

#Note
#The Benifit of multiprocessing is that  error or Memory leak in process won't hurt another process