from concurrent.futures import ThreadPoolExecutor
from time import sleep
import threading as t

 

# def cube(x):
#     print(x)
#     print(f'Cube of {x}:{2*x}')
#     return x

# if __name__ == '__main__':
#     result =[]
#     # with ThreadPoolExecutor(max_workers=5) as exe:
#     #     values = [[3,4,5,6]]
#     #     result = exe.map(cube,values)
#     p1 = t.Thread(target=cube, args=([1,2,3],))
#     p1.start()
#     p1.join()
#     print(x)


# import concurrent.futures
# if __name__ == "__main__":
#     with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#         executor.map(cube, [[1,2,3]])

# def task():
#     print("Executing the given task")
#     result = 0
#     i = 0
#     for i in range(10):
#         result = result + i
#     print("I: {}".format(result))
#     print("The task is executed {}".format(threading.current_thread()))

# def main():
#     executor = ThreadPoolExecutor(max_workers=3)
#     task1 = executor.submit(cube,[1,2,3])
#     task2 = executor.submit(cube,[1,2,3])

# main()


def foo(bar, result, index):
    print('hello {} {}'.format(index,bar))
    result[index] = str(index)

from threading import Thread

threads = [None] * 10
results = [None] * 10
print(results)

for i in range(len(threads)):
    threads[i] = Thread(target=foo, args=([1,2,3], results, i))
    threads[i].start()

for i in range(len(threads)):
    threads[i].join()

print(results)
print (" ".join(results))
