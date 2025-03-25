'''
Merging two Priority queues
'''
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def enqueue(self, value):
        heapq.heappush(self.heap, value)
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Priority Queue is empty")
        return heapq.heappop(self.heap)
    
    def peek(self):
        if self.is_empty():
            raise Exception("Priority Queue is empty")
        return self.heap[0]
    
    def size(self):
        return len(self.heap)
    
    def print_pq(self):
        if self.is_empty():
            print("Priority Queue is empty")
        else:
            print("Priority Queue (heap array):", self.heap)

def merge_priority_queues(pq1, pq2):
    merged_pq = PriorityQueue()
    
    # Move all elements from pq1 to merged_pq
    while not pq1.is_empty():
        merged_pq.enqueue(pq1.dequeue())
    
    # Move all elements from pq2 to merged_pq
    while not pq2.is_empty():
        merged_pq.enqueue(pq2.dequeue())
    
    return merged_pq


if __name__ == "__main__":
    # Create two Priority Queues
    pq1 = PriorityQueue()
    pq2 = PriorityQueue()
    
    # Add elements to pq1
    pq1.enqueue(1)
    pq1.enqueue(3)
    pq1.enqueue(5)
    
    # Add elements to pq2
    pq2.enqueue(2)
    pq2.enqueue(4)
    pq2.enqueue(6)
    
    # Print original queues
    print("Priority Queue 1:")
    pq1.print_pq()
    print("Priority Queue 2:")
    pq2.print_pq()
    
    # Merge the queues
    merged = merge_priority_queues(pq1, pq2)
    
    # Print merged queue
    print("\nMerged Priority Queue:")
    merged.print_pq()
    
    # Verify the order by dequeuing all elements
    print("Dequeuing all elements from merged queue:")
    while not merged.is_empty():
        print(merged.dequeue(), end=" ")
    print()