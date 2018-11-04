
class Stack:
    def __init__(self):
        self.stack=[]

    def add(self,data):
        self.stack.append(data)

    def peek(self):
        return self.stack[len(self.stack)-1]

    def pop(self):
        return self.stack.pop()

    def prints(self):
        for i in self.stack:
            print(i,)

def main():

    stack = Stack()
    for i in range(10):
        stack.add(i)

    stack.prints()
    p = stack.peek()
    print(p)
    stack.pop()
    print(stack.peek())
    stack.add(88)
    stack.prints()
    
main()        
