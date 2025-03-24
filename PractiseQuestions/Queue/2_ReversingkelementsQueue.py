'''
Reversing first K elements from the queue
'''
'''
Summary of Methods
| Method             | Time Complexity | Space Complexity | Notes                                      |
|--------------------|-----------------|------------------|--------------------------------------------|
| Using Stack        | (O(n)        |O(n)         | Most common and straightforward            |
| Using Recursion    | (O(n)        |O(n)         | Elegant but uses call stack                |
| Using Another Queue| (O(n^2)      |O(n)         | Inefficient, rarely used                   |
| In-Place (Array)   | (O(n)        |(O(1)        | Only if array access is allowed (unlikely) |

'''

class ReverseKQueue:
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
        if self.rear < len(self.queue):  # Reuse space if available
            self.queue[self.rear] = value
        else:
            self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise "Queue is empty.."
        removed_element = self.queue[self.front]
        if self.front == self.rear:
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
    
    # Stack based implementation
    def reverse_k_elements(self,k):
        if self.is_empty() or k > self.get_size() or k < 2: return
        stack = []
        # Step 1: Dequeue k elements into stack
        for _ in range(k):
            stack.append(self.dequeue())
        # Step 2: Create temp queue for remaining elements
        temp = ReverseKQueue()
        while not self.is_empty():
            temp.enqueue(self.dequeue())
        # Step 3: Enqueue reversed elements from stack
        while stack:
            self.enqueue(stack.pop())
        # Step 4: Enqueue remaining elements from temp
        while not temp.is_empty():
            self.enqueue(temp.dequeue())


    # def reverse_k_elements(self, k):
    #     #inplace reversal
    #     if self.is_empty() or k < 2 or k > self.get_size():
    #         return
    #     start = self.front
    #     end = self.front+ k-1 #formula for correct end, as front could be more than 0 (if dequeue)
    #     count = 0
    #     while count < k//2:
    #         self.queue[start], self.queue[end] = self.queue[end],self.queue[start]
    #         start +=1
    #         end -=1
    #         count +=1

class Main:
    @staticmethod
    def run():
        queue = ReverseKQueue() 
        for i in range(1,11):
            queue.enqueue(i*2 )

        queue.print_queue()
        k = int(input("Enter number of elements: "))
        print(f"\nAfter Reversing {k} elements...\n")
        queue.reverse_k_elements(k)

        queue.print_queue()

if __name__ == "__main__":
    Main.run()