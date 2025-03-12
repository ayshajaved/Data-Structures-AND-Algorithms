#Implementing the stack using the list
class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
    def push(self, value):
        self.top +=1
        if self.top < self.size():
            self.stack[self.top] = value
        else:
            self.stack +=[value]
    def peek(self):
        #returning the last top element of the stack
        if not self.isEmpty():
            return self.stack[self.top]
    def isEmpty(self):
        return self.size() ==0
    def pop(self):
        #deleting the top element also returning
        top = self.stack[self.top]
        self.top -=1
        self.stack.pop()
        return top
    def display(self):
        print(self.stack[::-1])
    def size(self):
        return len(self.stack)

class InfixToPostfix:
    def __init__(self):
        self.stack = Stack()
        self.postfix = []
    def precedence(self, operator):
        if operator in ('+', '-'):
            return 1
        elif operator in ('*', '/'):
            return 2
        elif operator in ('^'):
            return 3
        else:
            return 0
    def infix_to_postfix(self, expression):
        #Method to convert infix to postfix
        '''
        If there is a character, it will be pushed to the postfix, otherwise if it is a operator, pushed to stack, pushing check if the pop element has higher precendence then current character, that that element is pushed to postfix(list)
        '''
        for char in expression:
            if char.isalnum():
                #append to postfix
                self.postfix.append(char)
            elif char == '(':
                #If there is a starting bracket, push to the stack
                self.stack.push(char)
            elif char == ')':
                #Now we have to pop operators from the stack and append in the postfix until ( starting bracket
                while(not self.stack.isEmpty() and self.stack.peek()!='('):
                    self.postfix.append(self.stack.pop())
                self.stack.pop() #Remove the (, and the ending bracket was never pushed
            else:
                #if there come operator
                while(not self.stack.isEmpty() and self.precedence(self.stack.peek())>= self.precedence(char)):
                    self.postfix.append(self.stack.pop())
                self.stack.push(char)
            #POP remaining operators from stack to the postfix list
        while(not self.stack.isEmpty()):
            self.postfix.append(self.stack.pop())
        return ''.join(self.postfix)    
#Testing
# s = Stack()
# s.push(20)
# s.push(30)
# s.push(40)
# s.display()
# print(s.peek())
# s.pop()
# s.display()

#User Interface
print("**************************")
print("Converting Infix to PostFix")
print("**************************")

obj = InfixToPostfix()
infix_expression = input("Enter infix Expression: ")
print(f"\nYour postfix Expression for given infix {infix_expression} : ")
print(obj.infix_to_postfix(expression= infix_expression))
