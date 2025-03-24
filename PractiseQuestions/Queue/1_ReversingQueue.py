'''
Summary of Methods
| Method             | Time Complexity | Space Complexity | Notes                                      |
|--------------------|-----------------|------------------|--------------------------------------------|
| Using Stack        | (O(n)        |O(n)         | Most common and straightforward            |
| Using Recursion    | (O(n)        |O(n)         | Elegant but uses call stack                |
| Using Another Queue| (O(n^2)      |O(n)         | Inefficient, rarely used                   |
| In-Place (Array)   | (O(n)        |(O(1)        | Only if array access is allowed (unlikely) |

'''

class ReverseQueue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1
    
    def get_size(self):
        return len(self.queue)

    def is_empty(self):
        return self.front ==-1
    
    def enqueue(self, value):
        if self.is_empty():
            self.front +=1
            self.rear +=1
        else:
            self.rear +=1
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise "Queue is empty.."
        removed_element = self.queue[self.front]
        if self.get_size()==0:
            #last element is removed
            self.front = -1
            self.rear = -1
        else:
            self.front +=1
        return removed_element
    
    def print_queue(self):
        if self.is_empty():
            print("Queue cannot be printed.. It's empty")
        for i in range(self.front,self.get_size()):
            print(self.queue[i])
    
    def reverse_queue(self):
        #inplace reversal
        if self.get_size()<2:
            return
        start = self.front
        end = self.rear
        count = 0
        while count < self.get_size()//2:
            self.queue[start], self.queue[end] = self.queue[end],self.queue[start]
            start +=1
            end -=1
            count +=1

class Main:
    @staticmethod
    def run():
        queue = ReverseQueue() 
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        queue.enqueue(40)
        queue.enqueue(50)

        queue.print_queue()

        print("\nAfter Reversing...\n")
        queue.reverse_queue()

        queue.print_queue()

if __name__ == "__main__":
    Main.run()