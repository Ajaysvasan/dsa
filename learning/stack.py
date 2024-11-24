class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.top = None
    
    def push(self,data):
        if self.head == None:
            newNode = Node(data)
            self.head = self.top = newNode
        else:
            newNode = Node(data)
            self.top.next = newNode
            self.top = newNode
    
    def pop(self):
        if self.head == None:
            print("Stack underflow")
            return False 
        elif self.head == self.top:
            self.head = self.top = None
        else:
            temp = self.head
            while(temp.next!=self.top):
                temp = temp.next
            temp.next = None
            self.top = temp
    def display(self):
        temp = self.head
        while(temp!=None):
            print(temp.data,end=" ")
            temp = temp.next
stack = Stack()

for i in range(1,20):
    stack.push(i)
stack.display()

stack.pop()
print()
stack.display()