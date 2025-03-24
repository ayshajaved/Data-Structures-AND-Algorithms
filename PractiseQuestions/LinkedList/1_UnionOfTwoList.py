'''
Suppose there are two list with integer values A and B. Write an algorithm that creats another list C, that will contain all the elements of two list not the repeated elements.
'''
#Method 1 using by default functions
# class UnionOfTwoList:
#     def __init__(self):
#         self.C = []
#         self.A = set([2,4,5,67,2,90,34])
#         self.B = set([2,3,4,5,6,7,90,21])
#     def Union(self):
#         self.C = self.A.union(self.B)  #alternative self.C = self.A | self.B Symmetric difference
#         return self.C
# u = UnionOfTwoList()
# print(u.Union())

#Method 2 by manually implementing the logic
'''
Inefficient because there are two loops having the compleity of O(n2) as there are two loops
'''

# class UnionOfTwoList:
#     def __init__(self):
#         self.listA = [2,3,4]
#         self.listB = [1,2,3]
#         self.listC = [] #empty list to store the elements of both list, not repeated
#     def union(self):
#         for ele in self.listA:
#             if ele not in self.listC:
#                 self.listC.append(ele)
        
#         for ele in self.listB:
#             if ele not in self.listC:
#                 self.listC.append(ele)
#     def display(self):
#         print(self.listC)
#     def sort(self):
#         self.listC.sort()
# obj = UnionOfTwoList()
# obj.union()
# obj.display()
# obj.sort()
# obj.display()

#Method 3 Most efficient
class Union:
    def __init__(self, listA, listB):
        self.A = set(listA)
        self.B = set(listB)
        self.C = [] #Empty list
    
    def union(self):
        self.C = list(self.A | self.B)
        # self.C = list(self.A ^ self.B)
        #^ is the symmetric difference, that gives the elements that are not in both, elements that are only in one of the sets but not in both.
        return self.C
obj = Union([1,2,5,6,8],[1,2,3,4])
print(obj.union())