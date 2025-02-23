'''
A Linked List in Python is a data structure used to store a collection of elements, called nodes, where each node contains two parts:

Data: The actual value stored in the node.
Pointer (or Reference): A link to the next node in the list.

Unlike arrays or lists in Python, linked lists do not store elements in contiguous memory locations. Instead, each node is connected to the next, forming a chain. This makes insertion and deletion operations more efficient, especially for large datasets.

Types of Linked Lists:
Singly Linked List: Each node points to the next node only.
-Insertion or deletion at the beginning of the list is O(1).
-Insertion or deletion at the end of the list is O(n). Because you have to traversed through the whole linked   
list to reach the end.

Doubly Linked List: Each node points to both the next and previous nodes.
-Insertion or deletion at the beginning of the list is O(1).
-Insertion or deletion at the end of the list is O(1). Because you can easily reach the end of the linked list
by traversing from the last node to the first node.

Circular Linked List: The last node points back to the first node, forming a circle.
-Insertion or deletion at the beginning of the list is O(1).
-Insertion or deletion at the end of the list is O(1). Because you can easily reach the end of the linked list
by traversing from the last node to the first node.
'''
'''
******************
Single Linked List
******************
'''
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#Nodes are created but they are not linked, as their next parameter is None 
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

# Creating a linked list
n1.next = n2
n2.next = n3
n3.next = n4

#Traversing the linked list
#Head is not traversed because it won't get back then, hence the variable is declared to traverse
head = n1
currentNode = head 
while(currentNode is not None):
    print(currentNode.data)
    currentNode = currentNode.next
print("-----------------")

#Adding element at the begining
head = n1
n5 = Node(50) #to add it in the begining, we will add head's address to its next
n5.next = head
head = n5     #Now the head is this new node added at the beginning

#displaying the linkedlist
currentNode = n5
while(currentNode is not None):
    print(currentNode.data)
    currentNode = currentNode.next
print("-----------------")

#Adding element at the end
n6 = Node(60) #Node to be added at the end
currentNode = head
while(currentNode.next is not None):
    currentNode = currentNode.next
currentNode.next = n6

#Displaying the linkedlist
currentNode = head
while(currentNode is not None):
    print(currentNode.data)
    currentNode = currentNode.next
print("-----------------")

#Adding element at a specific position
#Add -100 in between 20 and 30
n7 = Node(-100)
currentNode = head
while(currentNode is not None and currentNode.data !=20):
    currentNode = currentNode.next
n7.next = currentNode.next
currentNode.next = n7

#Displaying the linkedlist
currentNode = head
while(currentNode is not None):
    print(currentNode.data)
    currentNode = currentNode.next
print("-----------------")

#Deleting the node
'''
In python, as there is dynamic memory allocation, so we just have to change the address of the next, and the node that is 
not pointing to any node will automatically be deallocated
'''
#Deleting from the start
head = head.next #50 is de allocated automatically
currentNode = head
#printing
while(currentNode is not None):
    print(currentNode.data)
    currentNode = currentNode.next
print("-----------------")

#Deleting node at the end
#Reach at the second last Node and set its next = none
currentNode = head
while(currentNode.next.next is not None):
    currentNode = currentNode.next
currentNode.next = None
#Displaying the linkedlist
currentNode = head
while(currentNode is not None):
    print(currentNode.data)
    currentNode = currentNode.next
print("-----------------")

#Deleting node at the specific position; delete 30
currentNode = head
while(currentNode.next.data !=30):
    currentNode = currentNode.next
currentNode.next = currentNode.next.next

#Displaying the linkedlist
currentNode = head
while(currentNode is not None):
    print(currentNode.data)
    currentNode = currentNode.next
print("-----------------")

#updating the 2nd node; to -20
currentNode = head
while(currentNode.next.data !=20):
    currentNode = currentNode.next
currentNode.next.data = -20

#displaying the linkedlist
currentNode = head
while(currentNode is not None):
    print(currentNode.data)
    currentNode = currentNode.next
print("-----------------")






        
