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


'''