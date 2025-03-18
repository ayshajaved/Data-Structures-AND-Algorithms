class ListNode:
    def __init__(self, data , next = None):
        self.data = data
        self.next = next
class Floyd:
    #Single Linked List
    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head
    
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
    
    #creating cycle
    def createCycle(self, value):
        current = self.head 
        while current is not None and current.data !=value:
            current = current.next
        node = current
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    #Detect cycle
    def detect_cycle(self):
        #Using Floyd's Algorithm of two pointers
        if not self.head:
            print("No list to detect cycle..")
            return
        #Two pointers
        slow = self.head
        fast = self.head
        cycle_found = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow ==fast:
                cycle_found = True
                break
        
        if not cycle_found:
            return self.head
        slow = self.head
        while slow !=fast:
            slow = slow.next
            fast = fast.next

        #both slow and fast are at the start
        cycle_start = slow
        return cycle_start
    
    def remove_cycle(self, cycle_start):
        pass

    #Method to display the list
    def printList(self, head):
        if not head:
            print("List is empty..")
            return
        currentNode = head
        result = []
        visited = set()  # To track visited nodes by their memory address
        while currentNode:
            if id(currentNode) in visited:  # Check if we've seen this node before
                result.append(f"{currentNode.data} (cycle detected)")
                break
            result.append(str(currentNode.data))
            visited.add(id(currentNode))  # Add node's memory address to visited set
            currentNode = currentNode.next
        print(" --> ".join(result))
        

#Testing The solution
list = Floyd()
list.appendNode(20)
list.appendNode(30)
list.appendNode(40)
list.appendNode(50)
list.appendNode(60)
list.appendNode(70)
list.appendNode(80)

#Creating cycle
list.createCycle(40) #creates cycle of 80 --> 40

#Printing list with cycle
list.printList(list.getHead())

#Detecting cycle
cycle_start = list.detect_cycle()
list.printList(cycle_start) #must print from 40
