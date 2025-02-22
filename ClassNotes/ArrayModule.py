'''
Array can be implemented in python using numpy and array module
'''
import array as ar
class ArrayOperations():
    def __init__(self):
        self.arr = ar.array('i', [])
    def createArray(self, data):
        self.arr = ar.array('i', data)
    # def addAtEnd(self, value):
    #     self.arr.append(value)
    # def addAtIndex(self, index, value):
    #     self.arr.insert(index, value)
    #Adding without using inbuilt function
    def addAtBeginning(self, value):
        self.arr = ar.array('i', [value]) + self.arr
    def addAtEnd(self, value):
        self.arr = self.arr + ar.array('i', [value])
    def addAtIndex(self, index, value):
        self.arr = self.arr[:index] + ar.array('i', [value]) + self.arr[index:]
    # def deleteAtEnd(self):
    #     self.arr.pop()
    # def deleteAtIndex(self, index):
    #     self.arr.pop(index)
    #Deleting without using inbuilt function
    def deleteAtEnd(self):
        self.arr = self.arr[:len(self.arr)-1]
    def deleteAtIndex(self, index):
        self.arr = self.arr[:index] + self.arr[index+1:]
    def updateAtIndex(self, index, value):
        self.arr[index] = value
    def displayArray(self):
        for i in range(0, len(self.arr)):
            print(self.arr[i], end = " ")
        print()
    #There comes value to be searched
    # def searchArray(self,value):
    #     index = self.arr.index(value)
    #     print("Value found at index", index)
    #Searching without using builtin functions
    def searchArray(self,value):
        for i in range(0, len(self.arr)):
            if self.arr[i] == value:
                print("Value found at index", i)
                return
        print("Value not found")
    def sortArray(self):
        self.arr.tolist()

#Array operations
obj = ArrayOperations()
obj.createArray([1, 2, 3, 4, 5])
obj.addAtEnd(6)
obj.addAtIndex(1,100)
obj.displayArray()
obj.deleteAtEnd()
obj.displayArray()
obj.deleteAtIndex(1)
obj.displayArray()

