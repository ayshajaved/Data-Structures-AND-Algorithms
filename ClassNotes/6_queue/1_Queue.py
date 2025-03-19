'''
Queue is the linear abstract data structure that follows the FIFO principle or LILO. It has to ends
--> Front
--> Rear
Enqueue operation can be done through rear end.
Dequeue operation can be done through front end.

Operations:
* Enqueue
* Dequeue
* Peek()/front element
* isFull()
* isEmpty()
'''
class Queue:
    def __init__(self):
        self.queue = [] 
        self.front = -1
        self.rear = -1
    def size(self):
        return len(self.queue)
    def isEmpty(self):
        return self.front == -1
    def Enqueue(self, value):
        if(self.front == -1):
            self.front +=1
            self.rear +=1
        else:
            self.rear +=1
        self.queue.append(value)
    def Dequeue(self):
        #Removing the element at front
        if self.isEmpty():
            print("Queue is empty!")
            return None
        removed_element = self.queue[self.front]
        if self.size() ==1:
            print("last element Removed.. Queue is empty now..")
            self.rear =-1
            self.front = -1
            self.queue=[]
        else:
            self.front +=1

        return removed_element
    def displayQueue(self):
        if not self.isEmpty():
            for i in range(self.front, self.size()):
                print(self.queue[i])
        else:
            print("Empty Queue..")
q = Queue()
q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
q.displayQueue()
q.Dequeue()
print("After Dequeue: ")
q.displayQueue()
q.Dequeue()
print("After Dequeue: ")
q.displayQueue()
q.Dequeue()
print("After Dequeue: ")
q.displayQueue()