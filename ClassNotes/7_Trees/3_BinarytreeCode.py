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
class BinaryTree:
    def __init__(self, value, left= None, right= None):
        #initializing the root node
        self.data = value
        self.left = None
        self.right = None
    #method to insert the node
    def addNode(self,value):
        if self.data:
            if value < self.data:
                if not self.left:
                    self.left = BinaryTree(value=value)
                else:
                    self.left.addNode(value)
            else:
                if not self.right:
                    self.right = BinaryTree(value=value)
                else:
                    self.right.addNode(value=value)
        else:
            self.data = value
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data, end=" ")
        if self.right:
            self.right.inorder_traversal()
    def preorder_traversal(self):
        print(self.data, end=" ")
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.data, end = " ")

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