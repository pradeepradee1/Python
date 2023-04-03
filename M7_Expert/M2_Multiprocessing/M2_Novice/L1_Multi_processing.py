from multiprocessing import Pool
import time

def f(n):
    print("n",n)
    sum = 1*n
    # for x in range(1):
    #     sum += x*x
    print(sum)
    return sum


if __name__ == "__main__":
    t1=time.time()
    p = Pool()
    result = p.map(f,[[1,2,3]])
    print(result)
    p.close()
    p.join()
    
    print("Pool took:",time.time()-t1)

    # t2=time.time()    # for x in range(1):
    #     sum += x*x

    # result=[]
    # for x in range(100000):
    #     result.append(f(x))
    
    # print("Serial Processing took:",time.time()-t2)
