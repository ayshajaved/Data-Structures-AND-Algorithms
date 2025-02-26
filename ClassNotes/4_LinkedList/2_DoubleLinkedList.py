#Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

#Double Linked List without using class and objects
# n1 = Node(10)
# n2 = Node(20)
# n1.next = n2
# n2.previous = n1

#Double Linked List class
class DLL:
    def __init__(self):
        #Initially the head of the Double Linked List is None
        self.head = None
    def length(self):
        count = 1
        currentNode = self.head
        while(currentNode is not None):
            count+=1
            currentNode = currentNode.next
        return count
    def appendNode(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
        else:
            currentNode = self.head
            while(currentNode.next is not None):
                currentNode = currentNode.next
            currentNode.next = n
            n.previous = currentNode
    #Adding node at any index
    def addNode(self, at, data):
        if(at < 0 or at > self.length()):
            print("Enter Valid Index..")
        elif(at ==0):
            node = Node(data)
            self.head.previous = node
            node.next = self.head
            self.head = node
        else:
            n = Node(data)
            currentNode = self.head
            for i in range(at-1):
                currentNode = currentNode.next
            n.next = currentNode.next
            n.previous = currentNode
            currentNode.next = n

    def displayList(self):
        currentNode = self.head
        while(currentNode is not None):
            print(currentNode.data)
            currentNode = currentNode.next
    def deleteNode(self, index):
        if (index <0 or index > (self.length())):
            print("Index is invalid..")
            return
        currentNode = self.head
        for _ in range(index-1):
            currentNode = currentNode.next
        currentNode.next.previous = currentNode
        currentNode.next = currentNode.next.next

    
list = DLL()
list.appendNode(10)
list.appendNode(20)
# list.displayList()
list.addNode(0,30)
list.addNode(2,40)
list.addNode(3,200)
list.displayList()
print("After Deleting..")
list.deleteNode(3)  #3rd node to be deleted starting from index 0
list.displayList()