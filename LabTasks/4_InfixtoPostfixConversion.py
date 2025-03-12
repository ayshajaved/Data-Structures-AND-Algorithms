'''
Lab Task: Application of Stack
Name : Ayesha Javed
Registeration number:SP24-BSE-020-B
'''
#Implementing the stack using the list
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def peek(self):
        #returning the last top element of the stack
        if not self.isEmpty():
            return self.stack[-1]
        return None
    def isEmpty(self):
        return self.size() ==0
    def pop(self):
        #deleting the top element also returning
        if not self.isEmpty():
            return self.stack.pop()
        return None
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
            expression = expression.replace(" ", "") #Excluding spaes
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
class EvaluatingPostfix:
    def __init__(self):
        self.stack = Stack()
    def evaluate_postfix(self, postfix_expression):
        for char in postfix_expression:
            if char.isdigit():
                self.stack.push(int(char))
            else:  # Operator
                b = self.stack.pop()
                a = self.stack.pop()
                if char == '+':
                    self.stack.push(a + b)
                elif char == '-':
                    self.stack.push(a - b)
                elif char == '*':
                    self.stack.push(a * b)
                elif char == '/':
                    self.stack.push(a / b)
        return self.stack.pop()
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
print("***************************")
print("Converting Infix to PostFix")
print("***************************")

obj = InfixToPostfix()
evaluator = EvaluatingPostfix()
infix_expression = input("Enter infix Expression: ")
print(f"\nYour postfix Expression for given infix {infix_expression} : ")
postfix_expression =obj.infix_to_postfix(expression= infix_expression)
print(postfix_expression)

print("*****************************")
print("Evaluating Postfix Expression")
print("*****************************")
print((evaluator.evaluate_postfix(postfix_expression)))