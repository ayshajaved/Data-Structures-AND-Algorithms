'''
Algorithm to find the duplicate elements in a Linkedlist
'''
'''
Method 1: Using hashset
- Time Complexity:
- Space Complexity: 
'''
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# class FindDuplicates:
#     def findDuplicate(self, head):
#         seen = set()
#         duplicates = set()
#         currentNode = head
#         while currentNode:
#             if currentNode.data in seen:
#                 duplicates.add(currentNode.data)
#             else:
#                 seen.add(currentNode.data)
#             currentNode = currentNode.next
#         return list(duplicates)
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(20)
# n4 = Node(40)
# n5 = Node(50)
# n6 = Node(10)
# n7 = Node(30)
# #Defining next
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
# n6.next = n7
# head = n1
# obj = FindDuplicates()
# print(obj.findDuplicate(head))

'''
Method 2: Brute force -Avoiding extra space
(O(n²) Time, O(1) Space)
This method uses two loops
'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class FindDuplicates:
    def findDuplicateNoSpace(self, head):
        duplicates = set()
        currentNode = head
        while currentNode and currentNode.next: #Checks if the list has only one node, then no dupliacte
            runner = currentNode.next
            while runner:
                if runner.data == currentNode.data:
                    duplicates.add(currentNode.data)
                runner = runner.next
            currentNode = currentNode.next
        return list(duplicates)
#Declaring nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(20)
n4 = Node(40)
n5 = Node(50)
n6 = Node(10)
n7 = Node(30)
#Defining next
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
head = n1
obj = FindDuplicates()
print(obj.findDuplicateNoSpace(head))