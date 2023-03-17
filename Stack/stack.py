"""
Stack Data structure
"""

class Stack():
    #   The constructor initialize py LIST
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]   #   Index pos -1 return the last of the list    
    
    def get_stack(self):
        return self.items

#   Creamos nuestro obj y asignamos items en el stack
myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")
myStack.push("D")
#print(myStack.peek())