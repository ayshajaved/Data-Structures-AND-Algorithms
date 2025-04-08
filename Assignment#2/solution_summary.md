# Emergency Room Management System Algorithm

## Purpose
Manage patient scheduling and treatment in an emergency room using a priority queue for normal cases and a double-ended queue (deque) for emergencies, ensuring critical patients and emergencies are treated first.

## Algorithm Steps

### 1. Initialization
- Create an empty **priority queue** to store patients based on priority and arrival order
- Create an empty **deque** for emergency patients
- Initialize an **order counter** to track patient arrival sequence

### 2. Add Patient
- **Input**: Patient type ("critical" or "non-critical"), unique ID
- **Steps**:
  1. Assign priority: 1 for critical, 2 for non-critical
  2. Create patient with ID, priority, and current order counter value
  3. Increment order counter
  4. Insert patient into priority queue (ordered by priority, then arrival order)

### 3. Declare Emergency
- **Input**: Patient ID
- **Steps**:
  1. Search priority queue for patient with matching ID
  2. Remove patient from priority queue
  3. Update patient:
     - Set emergency status to true
     - Change priority to 0 (highest)
  4. Add patient to front of emergency deque
  5. Output confirmation message

### 4. Treat Patient
- **Steps**:
  1. Check emergency deque:
     - If not empty, remove patient from front
     - Go to step 3
  2. Check priority queue:
     - If not empty, remove patient with highest priority (earliest arrival if tied)
     - If empty and no emergencies, output "No patients" and end
  3. Output treatment message with patient ID

### 5. Show Queue
- **Steps**:
  1. If both emergency deque and priority queue are empty, output "Queue: Empty" and end
  2. Build list of patient IDs:
     - Start with all patients in emergency deque (front to back)
     - Add all patients from priority queue (highest to lowest priority, earliest to latest arrival)
  3. Output list as comma-separated string

## Priority Rules
- Emergency (0) > Critical (1) > Non-Critical (2)
- Within same priority, earlier arrival (lower order counter) comes first

## Process Flow
1. Patients enter priority queue based on type
2. Emergency declaration moves patient to deque front
3. Treatment prioritizes deque, then queue
4. Queue display shows combined order

## Complexity
- **Add Patient**: O(log n) - priority queue insertion
- **Declare Emergency**: O(n) - linear search in queue
- **Treat Patient**: O(log n) - removal from queue or O(1) from deque
- **Show Queue**: O(n log n) - queue traversal
- **Space**: O(n) - storing n patients

---
*Generated on April 08, 2025*