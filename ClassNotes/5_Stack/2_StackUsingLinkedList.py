'''
Complexity must be O(1)
-Insertion or deletion from the single linked list would be from head so that the complexity should be O(1)
-Otherwise, from the end, there would be the complexity of O(n)
'''
class linkedNode:
    def __init__(self,data,next = None):
        self.data = data
class Stack:
    def __init__(self):
        self.top = 0