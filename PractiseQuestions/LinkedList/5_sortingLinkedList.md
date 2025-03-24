### Basic Linked List Structure
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
```

---

### 1. Bubble Sort
**How it works**: Repeatedly compares adjacent nodes and swaps them if they're in the wrong order until the list is sorted.

**Simplest Code**:
```python
def bubbleSort(self):
    if not self.head:
        return
    
    swapped = True
    while swapped:
        swapped = False
        current = self.head
        while current.next:
            if current.data > current.next.data:
                # Swap data (simplest way)
                current.data, current.next.data = current.next.data, current.data
                swapped = True
            current = current.next

# Test
llist = LinkedList()
llist.push(5); llist.push(2); llist.push(8); llist.push(1)
print("Before:"); llist.printList()
llist.bubbleSort()
print("After:"); llist.printList()
```
- **Time Complexity**: O(n²) - compares every pair multiple times
- **Space Complexity**: O(1) - just uses a few pointers
- **Understanding**: Like bubbles rising to the top, larger values move right with each pass.

---

### 2. Selection Sort
**How it works**: Finds the smallest element and puts it at the start, then repeats for the remaining list.

**Simplest Code**:
```python
def selectionSort(self):
    if not self.head:
        return
    
    current = self.head
    while current:
        min_node = current
        temp = current.next
        while temp:
            if temp.data < min_node.data:
                min_node = temp
            temp = temp.next
        # Swap data
        current.data, min_node.data = min_node.data, current.data
        current = current.next

# Test
llist = LinkedList()
llist.push(5); llist.push(2); llist.push(8); llist.push(1)
print("Before:"); llist.printList()
llist.selectionSort()
print("After:"); llist.printList()
```
- **Time Complexity**: O(n²) - searches whole list for minimum each time
- **Space Complexity**: O(1) - no extra space needed
- **Understanding**: Like picking the smallest card from a deck and placing it in order.

---

### 3. Insertion Sort
**How it works**: Builds a sorted list by taking one element at a time and inserting it in the right position.

**Simplest Code**:
```python
def insertionSort(self):
    if not self.head:
        return
    
    sorted_head = None
    current = self.head
    while current:
        next_node = current.next
        # Insert into sorted list
        if not sorted_head or sorted_head.data > current.data:
            current.next = sorted_head
            sorted_head = current
        else:
            temp = sorted_head
            while temp.next and temp.next.data < current.data:
                temp = temp.next
            current.next = temp.next
            temp.next = current
        current = next_node
    self.head = sorted_head

# Test
llist = LinkedList()
llist.push(5); llist.push(2); llist.push(8); llist.push(1)
print("Before:"); llist.printList()
llist.insertionSort()
print("After:"); llist.printList()
```
- **Time Complexity**: O(n²) - inserts each element by comparing with sorted portion
- **Space Complexity**: O(1) - uses only pointers
- **Understanding**: Like sorting cards in your hand, inserting each new card in the right spot.

---

### 4. Merge Sort
**How it works**: Divides the list into two halves, sorts them recursively, then merges them back together.

**Simplest Code**:
```python
def mergeSort(self, head):
    if not head or not head.next:
        return head
    
    # Split into two halves
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    slow.next = None
    
    # Recursively sort
    left = self.mergeSort(head)
    right = self.mergeSort(second)
    
    # Merge
    if not left:
        return right
    if not right:
        return left
    if left.data <= right.data:
        result = left
        result.next = self.mergeSort(left.next, right)
    else:
        result = right
        result.next = self.mergeSort(left, right.next)
    return result

def sort(self):
    self.head = self.mergeSort(self.head)

# Test
llist = LinkedList()
llist.push(5); llist.push(2); llist.push(8); llist.push(1)
print("Before:"); llist.printList()
llist.sort()
print("After:"); llist.printList()
```
- **Time Complexity**: O(n log n) - divides list in half each time
- **Space Complexity**: O(log n) - due to recursive call stack
- **Understanding**: Like splitting a deck of cards, sorting each half, then combining them in order.

---

### 5. Quick Sort
**How it works**: Picks a pivot, partitions the list around it, and recursively sorts the sublists.

**Simplest Code**:
```python
def quickSort(self, start, end):
    if start and start != end and start != end.next:
        # Partition and get pivot position
        pivot = start
        prev = start
        current = start.next
        while current != end.next:
            if current.data < pivot.data:
                prev = prev.next if prev.next != current else current
                prev.data, current.data = current.data, prev.data
            current = current.next
        if pivot != prev:
            pivot.data, prev.data = prev.data, pivot.data
        
        # Recursively sort
        self.quickSort(start, prev)
        self.quickSort(prev.next, end)

def sort(self):
    if not self.head:
        return
    # Find last node
    end = self.head
    while end.next:
        end = end.next
    self.quickSort(self.head, end)

# Test
llist = LinkedList()
llist.push(5); llist.push(2); llist.push(8); llist.push(1)
print("Before:"); llist.printList()
llist.sort()
print("After:"); llist.printList()
```
- **Time Complexity**: O(n log n) average, O(n²) worst case
- **Space Complexity**: O(log n) average due to recursion
- **Understanding**: Like picking a leader (pivot) and arranging everyone smaller before and larger after.

---

### Complexity Summary
| Algorithm     | Time Complexity       | Space Complexity | Key Feature                  |
|---------------|-----------------------|------------------|-----------------------------|
| Bubble Sort   | O(n²)                | O(1)            | Simple, swaps adjacent nodes |
| Selection Sort| O(n²)                | O(1)            | Finds minimum each time     |
| Insertion Sort| O(n²)                | O(1)            | Builds sorted list gradually|
| Merge Sort    | O(n log n)           | O(log n)        | Divides and conquers        |
| Quick Sort    | O(n log n) avg, O(n²) worst | O(log n) | Partitions around pivot     |

---

### Understanding Made Simple
1. **Bubble Sort**: Imagine people swapping places with their neighbor if they're taller until everyone’s in height order.
2. **Selection Sort**: Picture picking the shortest person each time and lining them up at the front.
3. **Insertion Sort**: Think of organizing books on a shelf, sliding each new book into its proper spot.
4. **Merge Sort**: Like splitting a messy pile of papers into smaller piles, sorting each, then combining them.
5. **Quick Sort**: Imagine picking a middle height and having everyone shorter go left, taller go right, then repeating.

Most efficient is merge sort