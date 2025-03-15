class ListNode:
    def __init__(self, data , next = None):
        self.data = data
        self.next = next
class Floyd:
    #Single Linked List
    def __init__(self):
        self.head = None

    #Method to add node in a single Linked List
    def appendNode(self, value):
        node = ListNode(value)
        #If its the first entry
        if not self.head:
            self.head = node 
            return
        #If second or so on
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = node
    
    #Method to display the list
    def printList(self):
        if not self.head:
            print("List is empty..")
            return
        currentNode = self.head
        result = []
        while currentNode:
            result.append(str(currentNode.data))
            currentNode = currentNode.next
        print(" --> ".join(result))
        

#Testing The solution
list = Floyd()
list.appendNode(20)
list.appendNode(30)
list.appendNode(40)
list.appendNode(50)
list.printList()


