class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SLL:
    def __init__(self):
        self.head = None
    def length(self):
        count = 0
        currentNode = self.head
        while currentNode is not None:
            count += 1
            currentNode = currentNode.next
        return count
    def addNode(self, index, data):
        if index < 0 or index > self.length():  
            print("Enter Valid Index..")
            return
        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = node
            return
        currentNode = self.head
        for i in range(index - 1): 
            currentNode = currentNode.next
        node.next = currentNode.next
        currentNode.next = node

    def displayList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next
    '''Reversing By Iterative in place method best space and time complexity O(1), There are also other methods, Recursive or stack but they have the complexity of O(n)'''
    def reverse(self):
        temp = None
        current = self.head
        while current is not None:
            next_node = current.next  
            current.next = temp       
            temp = current            
            current = next_node       
        self.head = temp

s = SLL()
s.addNode(0, 10)
s.addNode(1, 20)
s.addNode(2, 30)
s.addNode(3, 40)
s.displayList()
s.reverse()
print("Reversed List:")
s.displayList()
