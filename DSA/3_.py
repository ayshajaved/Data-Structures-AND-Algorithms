#Recursion and loop for fibonacci series implementing time-space tradeoff
from time import time
import tracemalloc as tm
#Loop Function(Less time, More Space)
def fib(n):
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n+1):
            a, b = b, a+b
        return b
# Recursive Function(More time, less Space)
# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
tm.start()
start_time = time()
print(fib(30))
end_time = time()
tm.stop()
print("Time taken by recursion: ", end_time - start_time)
print(tm.get_traced_memory())
print(tm.get_tracemalloc_memory())

#More Time/Less space       #Less time/More Space
#Recursive Function         #Loop Function
#Compressed Data            #Uncompressed Data
#Recalculation              #Lookup
#Rendering                  #Storage
   
