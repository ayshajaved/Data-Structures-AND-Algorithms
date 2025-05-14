'''Lab Task: Implement Binary Search Tree

Implement the following operations of BST:
• Insert in BST-place an element in the existing structure of BST.
• Search in BST-check about presence of an element in BST, if found returns number
of comparisons done for a successful search.
• Delete from BST-delete the element from BST
• Display BST/ Traversal-displays all the nodes in one of the three possible
traversals'''

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

    def search(self, value):
        return self._search_recursive(self.root, value, 0)

    def _search_recursive(self, node, value, comparisons):
        if node is None or node.value == value:
            return comparisons if node else -1
        comparisons += 1
        if value < node.value:
            return self._search_recursive(node.left, value, comparisons)
        return self._search_recursive(node.right, value, comparisons)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def display_inorder(self):
        if not self.root:
            print("Tree is empty")
        else:
            self._inorder_recursive(self.root)
            print()

    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.value, end=" ")
            self._inorder_recursive(node.right)

#Main method
class Main:
    @staticmethod
    def run():
        bst = BinarySearchTree()

        # Insert elements
        elements = [50, 30, 70, 20, 40, 60, 80]
        for element in elements:
            bst.insert(element)
        
        # Display tree
        print("Inorder traversal of BST:")
        bst.display_inorder()
        
        # Search elements
        search_values = [40, 90]
        for value in search_values:
            result = bst.search(value)
            if result >= 0:
                print(f"Found {value} after {result} comparisons")
            else:
                print(f"{value} not found in BST")
        
        # Delete elements
        delete_values = [30, 50]
        for value in delete_values:
            bst.delete(value)
            print(f"After deleting {value}, inorder traversal:")
            bst.display_inorder()
 
if __name__ == "__main__":
    Main.run()