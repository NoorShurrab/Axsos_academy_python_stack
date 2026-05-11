class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.Stack) != 0:
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")
        
    def peek(self):
        if len(self.Stack) != 0:
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")

