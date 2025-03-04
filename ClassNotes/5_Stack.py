'''
What is a Stack?
A stack is a linear data structure that follows the LIFO (Last In, First Out) principle. This means that the last element added to the stack will be the first one to be removed.

Operations:
1--> Push 
2--> Peek (Fetching the top element without removing)
3--> Pop  (Remove the top element)
4--> isempty (User-defined Function)
5--> size    (User-defined Function)
'''
class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        return len(self.stack) ==0
        
    def push(self, element):
        self.top +=1
        if(self.top < self.size()):
            self.stack[self.top] = element
        else:
            self.stack += [element]
    
    def pop(self):
        '''Removing the top element'''
        if not self.isEmpty():
            topItem = self.stack[self.top]
            self.top -=1
            return topItem
        return "Stack is Empty!..."
    
    def peek(self):
        '''Fetching the top element without removing'''
        if not self.isEmpty():
            topItem = self.stack[self.top]
            return topItem
        return "Stack is Empty!.."
    
    def display(self):
        if(self.top<0):
            print("Stack is Empty!...")
        '''1st method: Displaying of Stack in reverse order'''
        print("\nStack Displaying..\n")
        for i in range(self.top,-1, -1):
            print(f"|{self.stack[i]}|")
        '''2nd Method'''
        # print(self.stack[::-1])

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
'''Pushing the last element'''
s.display()
print(s.pop())
s.display()

'''Peeking the last element'''
print(s.peek())

'''Displaying'''
s.display()