'''
Circular Linked List is the single linked list, where there is a head and tail. 
Last node will have address of the first node
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def get_length(self):
        if not self.head:
            return 0
        count = 1
        temp = self.head
        while(temp.next != self.head):
            count+=1
            temp = temp.next
        return count
    def addNode(self, index, value):
        node = Node(value)
        if(index < 0 or index > self.get_length()):
            print("Invalid Index..")
        elif(index == 0):
            if(self.head is None):
                self.head = node
                self.tail = node
                node.next = node #circularly linked
            else:
                node.next = self.head
                self.tail.next = node
                self.head = node
        else:
            currentNode = self.head
            for _ in range(index-1):
                currentNode = currentNode.next
            node.next = currentNode.next
            currentNode.next = node
            if currentNode == self.tail:  # If inserting at last position, update tail
                self.tail = node
    def displayList(self):
        if(self.head is None):
            print("List is Empty!")
            return
        currentNode = self.head
        while(True):
            print(currentNode.data)
            currentNode = currentNode.next
            if currentNode == self.head:
                break
c = CLL()
c.addNode(0,10)
c.addNode(1,20)
c.addNode(2,40)
c.displayList()