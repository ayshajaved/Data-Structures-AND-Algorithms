'''
Emergency Room Patient Flow Management System
'''

#Node class
class ProcedureNode:
    def __init__(self, procedure):
        self.procedure = procedure
        self.next = None
        
class Patient:
    def __init__(self,id,name,priority, procedureList):
        self.id = id
        self.name = name
        self.priority = priority #1 for highest priority
        self.procedureList = procedureList
        
        if procedureList:
            self.procedureHead = ProcedureNode(procedureList[0])
            current =  self.procedureHead
            for pro in procedureList[1:]:
                current.next = ProcedureNode(pro)
                current = current.next            
class RoomPatientSystem:
    def __init__(self):
        self.patients = []
        
    def addPatient(self,id,name,priority, procedureList):       
        patient = Patient(id, name, priority, procedureList)
        i =0
        while i < len(self.patients) and self.patients[i].priority <= priority:
            i +=1       
        self.patients.insert(i, patient)
        print("Patient Added Successfully..")

    def getNextPatient(self):
        #remove and return the patient with highest priority
        if not self.patients:
            print("No Patient in the Queue..")
            return None
        patient = self.patients.pop(0)
        print("Patient done..with ",patient.id, patient.name, "Priority: ",patient.priority)
        return patient
    
    def viewQueue(self):
        #display the queue of the patients
        if not self.patients:
            print("No Patient in the Queue..")
            return
        print("Printing the current Patient Queue:\n")
        for patient in self.patients:
            print(f"ID: {patient.id} Name:{patient.name} Priority:{patient.priority}")    
    
    def findPatient(self,patientId):
        for i in range(len(self.patients)):
           if self.patients[i].id == patientId:
               return i #returning the id
        return -1
               
    def viewProcedureList(self,patientId):
        #Displaying the procedure list of a particular patient
        index = self.findPatient(patientId)
        if index == -1:
            print("No patient found with the index given..")
            return
        patient = self.patients[index]
        if not patient.procedureHead:
            print("No procedure for given patient..")
            return
        current = patient.procedureHead
        procedures = []          
        while current:
            procedures.append(current.procedure)
            current = current.next                
        print("Procedures of Patient are: ", procedures)
    
    def updateProcedure(self, patientId, procedure):
        #appending a new procedure
        index = self.findPatient(patientId)
        if index == -1:
            print("No patient found with the index given..")
            return
        patient = self.patients[index]
        if not patient.procedureHead:
            print("No procedure for given patient..")
            return
        current = patient.procedureHead
        while current.next:
            current = current.next  
        current.next = ProcedureNode(procedure)
    print("Procedure Appended..")        
    
    def completeProcedure(self,patientId):
        #moving the head so that first procedure is completed
        index = self.findPatient(patientId)
        if index == -1:
            print("No patient found with the index given..")
            return
        patient = self.patients[index]
        if not patient.procedureHead:
            print("No procedure for given patient..")
            return
        completed = patient.procedureHead.procedure
        patient.procedureHead = patient.procedureHead.next
        
        print("Procedure Completed..", completed)        
        # current = patient.procedureHead
        # patient.procedureHead = current.next
        
        # current = patient.procedureHead
        # procedures = []          
        # while current:
        #     procedures.append(current.procedure)
        #     current = current.next                
        # print("Procedures of Patient are: ", procedures)
    
    
    def removePatient(self, patientId):
        #removing patient from the priority Queue
        index = self.findPatient(patientId=patientId)
        if index == -1:
            print("No patient found..")
            return
        patient = self.patients.pop(index)
        print("Patient removed..",patient.id)
        
class Main:
    @staticmethod
    def run():
        manager = RoomPatientSystem()
        print("----------------------------------------------")
        print("Welcome to Room Patient Flow Management System")
        print("----------------------------------------------")
        print("Adding Patients..\n")
        manager.addPatient(101, "Ali", 2, ["X-Ray", "MRI"])
        manager.addPatient(102, "Ahmed", 1, ["ECG", "Blood Test"])
        manager.addPatient(103, "Asif", 3, ["Consultation"])

        manager.getNextPatient()
        #→ Ahmed (Priority: 1)

        print("\nViewing Procedure List of patient ID 101..")
        manager.viewProcedureList(101)
        # # #→ X-Ray -> MRI
        
        print("\nCompleting Procedure of patient ID 101..")
        manager.completeProcedure(101)
        # # #→ Procedure 'X-Ray' completed.

        print("\nViewing Procedure List of patient ID 101(updated)..")
        manager.viewProcedureList(101)
        # # #→ MRI

        print("\nUpdating Procedure List of patient ID 101..\n")
        manager.updateProcedure(101, "CT Scan")

        print("\nViewing Procedure List of patient ID 101(After Appending)..")
        manager.viewProcedureList(101)
        # # #→ MRI -> CT Scan

        print("\nViewing the Queue of all patients..")
        manager.viewQueue()
        # # #→ Ahmed (1), Ali (2), Asif (3)

        print("\nRemoving Patient having ID 101..")
        manager.removePatient (101)

        print("\nViewing the Queue after removing patient of ID 101../n")
        manager.viewQueue()
        # # #→ Ali (2), Asif (3)

if __name__ == "__main__":
    #running the main class having static run method implementing room patient flowq management system
    Main.run()