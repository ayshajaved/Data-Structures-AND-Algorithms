'''
Nodes are created for binary tree having data, left and right parameters.
- Root pointer is maintained like head in linkedlist
Operations:
node creation, insertion, traversal (inorder, preorder, postorder), and searching.
'''
#Tree Node is defined for the binary trees
class treeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, root_value):
        self.root = treeNode(root_value)
        
    #method to insert the node