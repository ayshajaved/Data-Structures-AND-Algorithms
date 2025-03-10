There are two types of data structures
- Linear (Stack, Queue, Linkedlist)
- Non-linear (Tress)
a-->c
|
b

- a is the parent node
- b and c are nodes
- Parent node has not any parent
- Leaf node/ external node is the node that has no child
- Non-leaf node/internal node is the node that has atleast one child
- Path: Sequence of consecutive edges from source node to destination node
- Level of the tree is the height of the tree but level of node is not equal to height of node
- Level of the node is equal to depth of the node
- N nodes = n-1 edges

'''
---

### **1. Tree**
A **tree** is a non-linear data structure consisting of nodes connected by edges. It follows a hierarchical structure where each node has a parent (except the root) and may have multiple children.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  # Left child
        self.right = None  # Right child
```

---

### **2. Root**
The **root** is the topmost node in a tree, from which all nodes descend.

```python
root = Node(10)  # Root node with value 10
```

---

### **3. Parent and Child**
- **Parent**: A node that has one or more children.
- **Child**: A node that has a parent.

```python
root.left = Node(5)  # 5 is a child of 10
root.right = Node(15)  # 15 is a child of 10
```

---

### **4. Sibling**
Nodes that share the same parent are called **siblings**.

```python
# 5 and 15 are siblings
```

---

### **5. Leaf Node**
A node that has no children is called a **leaf node**.

```python
leaf = Node(20)  # No left or right child
```

---

### **6. Edge**
An **edge** is the connection between two nodes.

```python
# root -> left (10 -> 5) is an edge
```

---

### **7. Depth**
The **depth** of a node is the number of edges from the root to that node.

```python
# Depth of root = 0
# Depth of 5 or 15 = 1
```

---

### **8. Height**
The **height** of a node is the number of edges on the longest path from that node to a leaf.

```python
# If the tree has 3 levels, height of root = 2
```

---

### **9. Degree**
The **degree** of a node is the number of children it has.

```python
# root (10) has degree 2 (children: 5, 15)
```

---

### **10. Subtree**
A **subtree** is a tree consisting of a node and its descendants.

```python
# The subtree rooted at 5 includes all its children
```

---

### **11. Binary Tree**
A **binary tree** is a tree in which each node has at most **two children** (left and right).

```python
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

---

### **12. Full Binary Tree**
A binary tree in which every node has either **0 or 2 children**.

---

### **13. Complete Binary Tree**
A binary tree in which all levels are completely filled except possibly the last, which is filled from left to right.

---

### **14. Perfect Binary Tree** 
A binary tree where all interior nodes have **two children**, and all leaf nodes are at the **same level**.

---

### **15. Balanced Binary Tree**
A binary tree where the **height difference between left and right subtrees of any node is at most 1**.

```python
def is_balanced(root):
    if not root:
        return 0
    left_height = is_balanced(root.left)
    right_height = is_balanced(root.right)
    return abs(left_height - right_height) <= 1
```

---

### **16. Degenerate (Skewed) Tree**
A tree where each parent has only **one child**, making it behave like a linked list.

---

### **17. Binary Search Tree (BST)**
A BST is a binary tree where:
- Left subtree contains nodes with values **less than** the node.
- Right subtree contains nodes with values **greater than** the node.

```python
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.value:
            if self.left is None:
                self.left = BST(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BST(data)
            else:
                self.right.insert(data)
```

---

### **18. AVL Tree**
A self-balancing BST where the height difference between left and right subtrees is at most **1**.

---

### **19. Red-Black Tree**
A self-balancing BST that follows **coloring rules** (red or black) to maintain balance.

---

### **20. B-Tree**
A self-balancing search tree designed for **large datasets** and databases.

---

### **21. N-ary Tree**
A tree where each node can have at most **N children**.

---

### **22. Traversal**
The process of visiting each node in the tree.
- **Inorder (Left, Root, Right)**
- **Preorder (Root, Left, Right)**
- **Postorder (Left, Right, Root)**
- **Level-order (BFS using a queue)**

```python
# Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

inorder(root)
```

---

### **23. Tree Depth**
The length of the longest path from the root to a leaf.

---

### **24. Ancestor**
A node that appears on the path from a given node to the root.

---

### **25. Descendant**
A node that appears below a given node in the tree.

---

### **26. LCA (Lowest Common Ancestor)**
The **lowest** node in the tree that is an ancestor of two given nodes.

```python
def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if left and right else left or right
```

---

### **27. Diameter of a Tree**
The **longest path** between any two nodes in a tree.

```python
def diameter(root):
    if not root:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    left_diameter = diameter(root.left)
    right_diameter = diameter(root.right)
    return max(left_height + right_height + 1, max(left_diameter, right_diameter))
```

---

### **28. Path Sum**
Finding a path in a tree where node values sum to a given number.

```python
def has_path_sum(root, target):
    if not root:
        return False
    if not root.left and not root.right and root.value == target:
        return True
    return has_path_sum(root.left, target - root.value) or has_path_sum(root.right, target - root.value)
```

---

