'''
Circular queue has the fixed size
- When we increament rear, if it is at add it will automatically points to the first index using this formular rear+1 % size
'''

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.size = 0
        self.front = -1
        self.rear = -1
    
    def enqueue(self,item):
        #adding elements in the queue
        if self.is_full():
            raise IndexError("Queue is Full..")
        if self.is_empty():
            self.front = 0
        #Increamenting the rear using the rear formula
        self.rear = (self.rear+1)% self.capacity
        self.queue[self.rear] = item
        self.size +=1

    def dequeue(self):
        #Removing the top element
        if self.is_empty():
            raise IndexError("Queue is empty..")

        item = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front+1)% self.capacity
        self.size-=1
        return item
    
    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size ==0 

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty...") 
        for i in range(self.front, self.size):
            print(self.queue[i])      
    
class Main():
    queue = CircularQueue(6)
    try:
        queue.enqueue(20)
        queue.enqueue(30)
        queue.enqueue(40)
        queue.enqueue(50)
        queue.enqueue(60)
        queue.enqueue(70)
        queue.print_queue()

        #Enquing when full
        queue.enqueue(80)
        #printing the queue
        queue.print_queue()
    except IndexError as e:
        print(f"{e}: Error")
    try:        
        print("\nDequeue...")
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()

        queue.dequeue()

        #Dequing when empty
        queue.dequeue()
    except IndexError as e:
        print(f"{e}: Error")

#Calling main method
if __name__ == "__main__":
    Main()
    

