#Pratical/Experimental study
from time import time
import tracemalloc as tm
#Solution 1           #this is the best solution according to time and space
def sumOf(n):
    return n*(n+1)/2

#Solution 2 
# def sumOf(n):
#     sum = 0
#     for i in range(n+1):
#         sum+=i
#     return sum
tm.start()
start_time = time()
print(sumOf(100000))
print(tm.get_traced_memory())
print(tm.get_tracemalloc_memory())
tm.stop()
end_time = time()
print(end_time - start_time)