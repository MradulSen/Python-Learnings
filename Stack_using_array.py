import array

class Stack:
    def __init__(self):
        self.my_stack = array.array('i',[])

    def is_empty(self):
        if len(self.my_stack):
            return False
        else:
            return True
        
    def push(self,element):
        self.my_stack.append(element)
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty can't pop")
        else:
            self.my_stack.pop()

if __name__== "__main__":
    stack = Stack()  #object in Python

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.my_stack)

    stack.pop()
    print(stack.my_stack)