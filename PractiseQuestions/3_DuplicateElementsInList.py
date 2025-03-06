'''
Algorithm to find the duplicate elements in an unsorted list
'''
'''
Method 1 Using Hashset()
Using extra space complexity O(n) and time O(n)
'''
# def findDuplicates(list):
#     seen = set()
#     duplicates = set()
#     for num in list:
#         if num in seen:
#             duplicates.add(num)
#         else:
#             seen.add(num)
#     return duplicates
# list1 = [1,2,4,5,6,4,3,2,1]
# print(findDuplicates(list= list1))

'''
Method 2: by sorting and comparing adjacent elements (less space)
- Time complexity O(n log n)
- Space complexity O(1)
'''
# def findDuplicates(list):
#     list.sort()
#     duplicates = []
#     for i in range(1, len(list)):
#         if(list[i] == list[i-1] and list[i] not in duplicates):
#             duplicates.append(list[i])

#     return duplicates

# list2 = [1,2,3,4,5,6,7,65,4,3,8]
# print(findDuplicates(list=list2))

'''
Method 3: Brute force - Compare every element with every other element
- Time Complexity O(n2)
- Space Complexity O(1)
'''

def findDuplicates(l):
    duplicates = set()
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] == l[j]:
                duplicates.add(l[i])

    return list(duplicates)

list3 = [1,2,3,4,7,8,9,8,7,3,46]
print(findDuplicates(list3))

