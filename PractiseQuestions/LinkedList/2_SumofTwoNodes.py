# '''
# Let k is the integer value and we have to write the algorithm tha will find the two nodes having sum equal to k without consuming extra space
# '''
# #Solution -> Two pointer technique
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Sll:
    def __init__(self):
        self.head = None
    def size(self):
        count = 0
        currentNode = self.head
        while(currentNode != None):
            count +=1
            currentNode = currentNode.next
        return count
    def addNode(self, index, value):
        if index < 0 or index > self.size():
            print("Index is out of bound..")
            return
        node = Node(value)
        if index ==0:
            node.next = self.head
            self.head = node
            return
        currentNode = self.head
        for i in range(index -1):
            currentNode = currentNode.next
        node.next = currentNode.next
        currentNode.next = node
    def display(self):
        currentNode = self.head
        while(currentNode is not None):
            print(currentNode.data, "->", end = " ")
            currentNode = currentNode.next
    def findPairWithSum(self, k): #worst O(n2)
        #Two pointers left and right
        tail = self.head
        #Traversing to the end for right
        while tail and tail.next:
            tail = tail.next
        left = self.head
        right = tail
        #Finding the sum if they are equal to k
        while left != right:
            currentSum = left.data + right.data
            if(currentSum ==k):
                return f"({left.data},{right.data})"
            elif( currentSum < k):
                left = left.next #Move Forward
            else:
                right = self.getPrevious(self.head, right)  #Move backward
        print("No Pair Found..")
    def getPrevious(self, head, node): #O(n)
        current = head
        while current and current.next != node:
            current = current.next
        return current

obj = Sll()
obj.addNode(0,1)      
obj.addNode(1,2)      
obj.addNode(2,5)
obj.addNode(3,6)
obj.addNode(4,8)
obj.display()      
print()
print(obj.findPairWithSum(11))

'''
Finding pair with the sum of K using the single Linked List has the worst case time complexity due to previous method and can be optimised into DLL
'''