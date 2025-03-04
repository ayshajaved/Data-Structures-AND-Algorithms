class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DLL:
    def __init__(self):
        self.head = None

    def length(self):
        count = 0
        currentNode = self.head
        while currentNode is not None:
            count += 1
            currentNode = currentNode.next
        return count

    def appendNode(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = n
            n.previous = currentNode

    def addNode(self, at, data):
        if at < 0 or at > self.length():
            print("Enter a valid index..")
            return
        n = Node(data)
        # Case 1: Adding at the head (index 0)
        if at == 0:
            if self.head is None:
                self.head = n
            else:
                n.next = self.head
                self.head.previous = n
                self.head = n
            return

        # Case 2: Adding elsewhere in the list
        currentNode = self.head
        for _ in range(at - 1):
            currentNode = currentNode.next

        n.next = currentNode.next
        n.previous = currentNode
        if currentNode.next:
            currentNode.next.previous = n
        currentNode.next = n

    def displayList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, end=" ")
            currentNode = currentNode.next
        print()

    def deleteNode(self, index):
        if index < 0 or index >= self.length():
            print("Index is invalid..")
            return
        
        # Case 1: Deleting the head node
        if index == 0:
            if self.head.next:
                self.head = self.head.next
                self.head.previous = None
            else:
                self.head = None  # List becomes empty
            return

        currentNode = self.head
        for _ in range(index - 1):
            currentNode = currentNode.next
        targetNode = currentNode.next
        currentNode.next = targetNode.next
        if targetNode.next:
            targetNode.next.previous = currentNode

    def reverse(self):
        currentNode = self.head
        temp = None
        while currentNode:
            temp = currentNode.previous
            currentNode.previous = currentNode.next
            currentNode.next = temp
            currentNode = currentNode.previous
        if temp:
            self.head = temp.previous

# Testing the corrected code
d = DLL()
d.addNode(0, 1)
d.addNode(1, 2)
d.addNode(2, 3)
d.displayList() 
d.reverse()
d.displayList()
