import random
# Defining the node for the tree
class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
# Defining the tree with it's operations 
class BinaryTree:
    def __init__(self):
        self.root = None

    # Inserting values 
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.insert_node(data,self.root)
    def insert_node(self,data,node):
        if node.data > data:
            if node.leftChild == None:
                node.leftChild = Node(data)
            else:
                self.insert_node(data,node.leftChild)
        else:
            if node.rightChild == None:
                node.rightChild = Node(data)
            else:
                self.insert_node(data,node.rightChild)
    # Displaying elements
    def inOrderTraversal(self,node,result=[]):
        if node:
            self.inOrderTraversal(node.leftChild,result)
            result.append(node.data)
            self.inOrderTraversal(node.rightChild,result)
        return result
    # Searching an element in a Binary Tree
    def search(self,node,target):
        if node is None:
            print("The element is not Found")
            return False
        else:
            if node.data == target:
                print("The element is Found")
                return
            elif node.data>target:
                self.search(node.leftChild,target)
            else:
                self.search(node.rightChild,target)
tree = BinaryTree()

values = [7, 4, 9, 1, 6, 8, 10]
for value in values:
    tree.insert(value)

print(tree.inOrderTraversal(tree.root))

tree.search(tree.root,11)