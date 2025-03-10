'''
Binary can be a tree having only a root tree.(No children)
It may be a tree having one node
But can't be having more than two children

Properties:
- At nth level, max number of nodes possible in a binary tree are 2^n
- Maximum number of nodes at height h = 2^h+1 -1
- Minimum number of nodes at height h = h+1
'''

# **1. Full Binary Tree**
### **Definition:**
A binary tree in which **each node has either 0 or 2 children**.

### **Example:**
```
       1
      / \
     2   3
    / \
   4   5
```
### **Important Parts:**
- Every node has **exactly two or zero children**.
- No node has only one child.

### **Python Implementation:**
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
```

---

# **2. Complete Binary Tree**
### **Definition:**
A binary tree in which **all levels are completely filled except possibly the last level**, which is **filled from left to right**.

### **Example:**
```
       1
      / \
     2   3
    / \  /
   4   5 6
```
### **Important Parts:**
- All levels except the last are **completely filled**.
- The last level is **filled from left to right**.

### **Python Implementation:**
```python
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
```

---

# **3. Perfect Binary Tree**
### **Definition:**
A binary tree in which **all internal nodes have exactly two children**, and **all leaf nodes are at the same level**.

### **Example:**
```
       1
      / \
     2   3
    / \  / \
   4   5 6  7
```
### **Important Parts:**
- Every **internal node** has **exactly two children**.
- All **leaf nodes** are at the **same level**.

### **Python Implementation:**
```python
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
```

---

# **4. Balanced Binary Tree**
### **Definition:**
A binary tree in which the **difference between the heights of the left and right subtrees of every node is at most 1**.

### **Example:**
```
       1
      / \
     2   3
    / \
   4   5
```
### **Important Parts:**
- The **height difference** between the left and right subtrees is **≤ 1**.
- Helps in **efficient searching**.

### **Python Implementation:**
```python
def is_balanced(root):
    if not root:
        return 0
    left_height = is_balanced(root.left)
    right_height = is_balanced(root.right)
    return abs(left_height - right_height) <= 1
```

---

# **5. Degenerate (Skewed) Binary Tree**
### **Definition:**
A binary tree in which **each parent node has only one child**, making it behave like a **linked list**.

### **Example (Left-Skewed Tree):**
```
    1
   /
  2
 /
3
/
4
```
### **Example (Right-Skewed Tree):**
```
1
 \
  2
   \
    3
     \
      4
```
### **Important Parts:**
- **Left-skewed**: Each node has **only a left child**.
- **Right-skewed**: Each node has **only a right child**.
- **Inefficient for searching** (degrades to **O(n)**).

### **Python Implementation:**
```python
root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.left.left = Node(4)
```

---

# **6. Binary Search Tree (BST)**
### **Definition:**
A binary tree where:
- **Left subtree** contains nodes with values **less than** the parent.
- **Right subtree** contains nodes with values **greater than** the parent.

### **Example:**
```
       10
      /  \
     5   20
    / \  /  \
   3   7 15  25
```
### **Important Parts:**
- Used for **fast searching** (O(log n) in average case).
- **Left subtree** → Smaller values.
- **Right subtree** → Larger values.

### **Python Implementation:**
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

root = BST(10)
root.insert(5)
root.insert(20)
root.insert(3)
root.insert(7)
root.insert(15)
root.insert(25)
```

---

# **7. AVL Tree**
### **Definition:**
A **self-balancing BST** where the **height difference** (balance factor) between left and right subtrees is at most **1**.

### **Important Parts:**
- Automatically **balances** after insertion or deletion.
- **Maintains O(log n) operations**.

---

# **8. Red-Black Tree**
### **Definition:**
A **self-balancing BST** that follows these rules:
1. **Each node is either red or black**.
2. **Root is always black**.
3. **Red nodes cannot have red children**.
4. **Every path from root to leaf must have the same number of black nodes**.

### **Important Parts:**
- Used in **databases and operating systems**.
- **Ensures logarithmic time complexity**.

---

# **9. B-Tree**
### **Definition:**
A **self-balancing search tree** used in **databases and file systems**.

### **Important Parts:**
- Each node can have **more than 2 children**.
- **Fast access to large datasets**.

---

# **10. N-ary Tree**
### **Definition:**
A tree where **each node can have up to N children**.

### **Example (Ternary Tree - N=3):**
```
       1
    /  |  \
   2   3   4
```
### **Important Parts:**
- Used in **file systems** and **AI (game trees)**.

### **Python Implementation:**
```python
class NaryNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # List of children

root = NaryNode(1)
root.children.append(NaryNode(2))
root.children.append(NaryNode(3))
root.children.append(NaryNode(4))
```

---

## **Summary of Binary Tree Types**
| **Type** | **Description** |
|----------|---------------|
| **Full Binary Tree** | Each node has 0 or 2 children |
| **Complete Binary Tree** | All levels except the last are full, last level is left-filled |
| **Perfect Binary Tree** | All leaf nodes are at the same level |
| **Balanced Binary Tree** | Height difference between left and right is ≤1 |
| **Degenerate Tree** | Every node has only one child |
| **Binary Search Tree (BST)** | Left < Root < Right |
| **AVL Tree** | Self-balancing BST (Height balance ≤1) |
| **Red-Black Tree** | Self-balancing BST with red/black coloring rules |
| **B-Tree** | Multi-child tree used in databases |
| **N-ary Tree** | Each node can have N children |

