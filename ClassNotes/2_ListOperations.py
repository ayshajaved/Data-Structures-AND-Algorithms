class ArrayOperations():
    def __init__(self):
        self.array = []
        self.size = 10
        #manually initialize the array with 10 elements
        self.array = [0] * self.size

    def create(self, data):
        #initialize the array with the given data
        for i in range(len(data)):
            self.array[i] = data[i]
        self.size = len(data)
    def addAtEnd(self, value):
        self.array[self.size] = value
        self.size += 1
    def addAtIndex(self, index, value):
        # Check if the index is valid
        if index <0 or index >= self.size:
            # Return an error message if the index is invalid
            return "Invalid index"
        else:
            self.array[index] = value
    def display(self):
        return self.array

    def update(self, index, value): 
        # Check if the index is valid
        if index <0 or index >= self.size:
            # Return an error message if the index is invalid
            return "Invalid index"
        else:
            self.array[index] = value

    def delete(self, index):
        # Check if the index is valid
        if index <0 or index >= self.size:
            # Return an error message if the index is invalid
            return "Invalid index"
        else:
            # Shift elements to the left to fill the gap
            for i in range(index, self.size - 1):
                self.array[i] = self.array[i + 1]   
            self.size -= 1
            self.array[self.size] = 0
#Testing Operations
a = ArrayOperations()
a.create([1,2,3,4,5])
print(a.display()) 
a.addAtEnd(200)
print(a.display()) 
a.addAtIndex(2, 100)
print(a.display())
a.delete(3)
print(a.display())
a.delete(3)
print(a.display())