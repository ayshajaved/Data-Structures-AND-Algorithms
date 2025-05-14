'''
Problem: Print Nodes in Range [L, R] in BST
Description: Print all elements of the BST that lie in the range [L, R] in increasing order.
Example:
BST: 10, 5, 1, 7, 15, 12, 18
Range: [6, 15] → Output: 7 10 12 15
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

    def print_nodes_in_range(self, L, R):
        print(f"Nodes in range [{L}, {R}]:", end=" ")
        self._print_nodes_in_range_recursive(self.root, L, R)
        print()

    def _print_nodes_in_range_recursive(self, node, L, R):
        if node is None:
            return
        # If node value is less than L, skip left subtree
        if node.value < L:
            self._print_nodes_in_range_recursive(node.right, L, R)
        # If node value is greater than R, skip right subtree
        elif node.value > R:
            self._print_nodes_in_range_recursive(node.left, L, R)
        # If node value is in range, process both subtrees and print node
        else:
            self._print_nodes_in_range_recursive(node.left, L, R)
            print(node.value, end=" ")
            self._print_nodes_in_range_recursive(node.right, L, R)

#Main class
class Main:
    @staticmethod
    def run():
        bst = BinarySearchTree() 
        elements = [20, 10, 30, 5, 15, 25, 35]
        for element in elements:
            bst.insert(element)
        bst.print_nodes_in_range(12, 32)

#Running main
if __name__ == "__main__":
   Main.run()