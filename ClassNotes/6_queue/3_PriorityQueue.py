'''
Priority queue exceute the dequeue function according to the priority of the task
- Heap will be used for this purpose
- Python heapq will be used
'''
import heapq
class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,priority,item):
        heapq.heappush(self.queue,(priority, item))
    
    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)[1]
        raise IndexError("Queue is empty..")
    
    def is_empty(self):
        return len(self.queue) ==0
    
    def print_queue(self):
        # print(sorted(self.queue))
        print(self.queue)
     
class Main:
    queue = PriorityQueue()
    try:
        queue.enqueue(3,"Drink")
        queue.enqueue(1,"Smile")
        queue.enqueue(4,"Work")
        queue.enqueue(2,"Eat")
    
        #Printing Queue
        '''
        Printing the heap will print not in sorted form, rather in a heap data structure, following the parent(mini) as root and then children(traversal), we can resolve it by using sorted() function in print_queue() method
        '''
        queue.print_queue()

        #Dequeue
        print(queue.dequeue())
        print(queue.dequeue())
        print(queue.dequeue())
        print(queue.dequeue())

    except IndexError as e:
        print(f"Error: {e}")