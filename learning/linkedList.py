MESSAGE = "The list is empty"

# Creating a class called node

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Creating Linked List

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    # To Check if the list is empty
    def isEmpty(self):
        if self.head == None:
            return True
        return False
    # To insert an element at the begining 
    def insertElementAtBegining(self,data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.count+=1
    # To insert the element at the end
    def insertElementAtEnd(self,data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next = node
        self.count+=1
    
    # To insert an element at a given position i where i ranges from 1 to n
    # So while taking that into account we have to insert the element in the pos = i-1
    def insertElememtAtPosition(self,data,pos):
        if pos-1==0:
            self.insertElementAtBegining(data)
        elif pos-1==self.count:
            self.insertElementAtEnd(data)
        elif pos-1!=0 and pos-1!=self.count:
            node = Node(data)
            temp = self.head
            for _ in range(pos-2):
                temp = temp.next
            node.next = temp.next
            temp.next = node
        self.count+=1

    # Deleting the element at the start of the list
    def deleteAtBegining(self):
        if self.head == None:
            print(MESSAGE)
        else:
            self.head = self.head.next
            self.count-=1
    
    # Deleting the element at the end of the list
    def deleteAtEnd(self):
        if self.isEmpty():
            print(MESSAGE)
        else:
            temp = self.head
            while temp.next.next !=None:
                temp = temp.next
            temp.next = None
            self.count-=1
    # Before getting into the next function we need to define the search function
    def search(self,target):
        if self.isEmpty():
            print(MESSAGE)
        else:
            pos = 0
            temp = self.head
            while temp!=None:
                if temp.data  == target:
                    return pos
                temp = temp.next
                pos+=1
            return -1
    # Deleting the element a given element 
    def deleteAtPosition(self,target):
        pos = self.search(target)
        if self.isEmpty():
            print(MESSAGE)
        elif pos==-1:
            print("The element is not in the list")
        else:
            temp = self.head
            for i in range(pos-1):
                temp = temp.next
            temp.next = temp.next.next
            self.count-=1
        


    
    # Displaying the elements
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data,end=" ")
            temp = temp.next

List = LinkedList()
for i in range(1,21):
    List.insertElementAtBegining(i)
List.insertElementAtEnd(30)
List.insertElememtAtPosition(21,4)

List.display()
print()

List.deleteAtBegining()
List.deleteAtEnd()
List.deleteAtPosition(21)

List.display()