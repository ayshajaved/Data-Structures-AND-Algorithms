#importing required libraries
from collections import deque
from queue import PriorityQueue

#Patient Class
class Patient:
    def __init__(self, id, priority, arrival_order):
        self.id = id
        # Priority: 0 for emergency (highest), 1 for critical, 2 for non-critical
        self.priority = priority  
        self.arrival_order = arrival_order
        self.is_emergency = False
    
    # For priority queue comparison
    def __lt__(self, other):
        # If one is emergency and other isn't, emergency comes first
        if self.is_emergency != other.is_emergency:
            return self.is_emergency
        # Otherwise compare priority, then arrival order
        if self.priority != other.priority:
            return self.priority < other.priority
        return self.arrival_order < other.arrival_order

class ERManagementSystem:
    def __init__(self):
        self.pq = PriorityQueue()  # Priority queue for normal scheduling
        self.emergency_deque = deque()  # Deque for emergency cases
        self.order_counter = 0  # To track arrival order
        self.patients = {}  # Dictionary to track all patients by ID

    def addPatient(self, type, id):
        #adding patient
        if id in self.patients:
            print(f"Patient {id} already exists")
            return
        
        # Set priority based on type
        priority = 1 if type == "critical" else 2
        patient = Patient(id, priority, self.order_counter)
        self.order_counter += 1
        self.patients[id] = patient
        self.pq.put(patient)

    def declareEmergency(self, id):
        #Patient as emergency and moving to front
        if id not in self.patients:
            print(f"Patient {id} not found")
            return
        
        # Create temporary queue to find and remove patient
        temp_queue = PriorityQueue()
        patient_found = None
        
        while not self.pq.empty():
            patient = self.pq.get()
            if patient.id == id:
                patient_found = patient
            else:
                temp_queue.put(patient)
        
        # Restore non-emergency patients to priority queue
        while not temp_queue.empty():
            self.pq.put(temp_queue.get())
        
        if patient_found:
            patient_found.is_emergency = True
            patient_found.priority = 0  # Set highest priority
            self.emergency_deque.appendleft(patient_found)
            print(f"Emergency declared: {id} moved to the front")

    def treatPatient(self):
        #Treating patient next in the queue
        if not self.emergency_deque and self.pq.empty():
            print("No patients in queue")
            return
        
        # Check emergency deque first
        if self.emergency_deque:
            patient = self.emergency_deque.popleft()
        else:
            patient = self.pq.get()
        
        print(f"Treating patient {patient.id}")
        del self.patients[patient.id]

    def showQueue(self):
        #Display current queue status
        if not self.emergency_deque and self.pq.empty():
            print("Queue: Empty")
            return
        
        queue_list = []
        # Add emergency patients first
        for patient in self.emergency_deque:
            queue_list.append(patient.id)
        
        # Add remaining patients from priority queue
        temp_queue = PriorityQueue()
        while not self.pq.empty():
            patient = self.pq.get()
            queue_list.append(patient.id)
            temp_queue.put(patient)
        
        # Restore priority queue
        while not temp_queue.empty():
            self.pq.put(temp_queue.get())
        
        print("Queue: " + ", ".join(queue_list))

# Test the implementation
class Main:
    @staticmethod
    def run():
        try:
            er = ERManagementSystem()
            # Test cases from example
            er.addPatient("critical", "P1")
            er.addPatient("non-critical", "P2")
            er.addPatient("critical", "P3")
            er.treatPatient()  # Treats P1
            er.addPatient("non-critical", "P4")
            er.declareEmergency("P4")
            er.showQueue()
            er.treatPatient()  # Treats P4
            er.treatPatient()  # Treats P3
    
        except Exception as e:
            print("Error: ", e)

if __name__ == "__main__":
    Main.run()