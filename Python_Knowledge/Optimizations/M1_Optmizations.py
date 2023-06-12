#FirstWay
print("1st Way")
randomlist=[23,45,23,12,33]
counter=0
for val in randomlist:
    print(counter,val)
    counter+=1

print("2nd Way")
#SecondWay
for val in range(len(randomlist)):
    print(val,randomlist[val])

print("3rd Way")
#Thirds Way is efficient and faster
for i,val in enumerate(randomlist):
    print(i,val)
