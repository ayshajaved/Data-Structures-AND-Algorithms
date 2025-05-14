'''
Write down code to print and count Leaf nodes of a BST.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def print_leaf_nodes(self):
        print("Leaf nodes:", end=" ")
        self._print_leaf_nodes_recursive(self.root)
        print()

    def _print_leaf_nodes_recursive(self, node):
        if node:
            if not node.left and not node.right:
                print(node.value, end=" ")
            self._print_leaf_nodes_recursive(node.left)
            self._print_leaf_nodes_recursive(node.right)

    def count_leaf_nodes(self):
        return self._count_leaf_nodes_recursive(self.root)

    def _count_leaf_nodes_recursive(self, node):
        if node is None:
            return 0
        if not node.left and not node.right:
            return 1
        return (self._count_leaf_nodes_recursive(node.left) +
                self._count_leaf_nodes_recursive(node.right))
#Main class having main method
class Main:
    @staticmethod
    def run():
        bst = BinarySearchTree()
        # Insert elements
        elements = [50, 30, 70, 20, 40, 60, 80]
        for element in elements:
            bst.insert(element)
        
        # Print leaf nodes
        bst.print_leaf_nodes()
        
        # Count leaf nodes
        leaf_count = bst.count_leaf_nodes()
        print(f"Number of leaf nodes: {leaf_count}")
        
#Running main method
if __name__ == "__main__":
    Main.run()