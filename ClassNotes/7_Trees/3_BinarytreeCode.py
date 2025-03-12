'''
Nodes are created for binary tree having data, left and right parameters.
- Root pointer is maintained like head in linkedlist
Operations:
node creation, insertion, traversal (inorder, preorder, postorder), and searching.
- Inorder (left--node--right)
- postorder (Left, Right, Root)
- preorder (Root, Left, Right)
'''
#Tree Node is defined for the binary trees
class Node:
    def __init__(self,value,left= None, right= None):
        self.value = value
        self.left = None
        self.right = None   
    #method to insert the node
    def addNode(self,value):
        if value < self.value:
            if not self.left:
                self.left = Node(value=value)
            else:
                self.left.addNode(value)
        else:
            if not self.right:
                self.right = Node(value=value)
            else:
                self.right.addNode(value=value)
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value, end=" ")
        if self.right:
            self.right.inorder_traversal()
    def preorder_traversal(self):
        print(self.value, end=" ")
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value, end = " ")
    def searchNode(self, key):
        #Iterative search
        current = self #Current node
        while current:
            if key == current.value:
                return self #Current node found
            elif key < current.value:
                current = current.left
            elif key > current.value:
                current = current.right
        return None

class BinaryTree:
    def __init__(self, value):
        #initializing the root node
        self.root = Node(value)
    def addNode(self, value):
        self.root.addNode(value=value)
    def inorder_traversal(self):
        self.root.inorder_traversal()
        print()
    def preorder_traversal(self):
        self.root.preorder_traversal()
        print()
    def postorder_traversal(self):
        self.root.postorder_traversal()
        print()
    def searchNode(self, key):
        return self.root.searchNode(key)    

#Testing
tree = BinaryTree(10) #Inilializing root node
tree.addNode(20) #will be inserted in right
tree.addNode(5)  #will be inserted in left        
tree.addNode(30)
tree.addNode(40)
tree.addNode(4)
tree.addNode(3)

#Traversal
#Left-root-right
print("\n**Inorder Traversal**")
tree.inorder_traversal()

#preorder(root-left-right)
print("\n**ُPreorder Traversal**")
tree.preorder_traversal()

#PostOrder Traversal
print("\n**ُPostorder Traversal**")
tree.postorder_traversal()

#Searching
print("------------------------")
print("Binary Search")
key = int(input("Enter Key: "))
print(f"Found: {key}" if tree.searchNode(key) else "Not Found")