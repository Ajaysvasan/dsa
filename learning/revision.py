from collections import defaultdict

# Creating Binary Search Tree

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self,data,node):
        if self.root == None:
            self.root = TreeNode(data)
        else:
            self.insert_recursive(data,node)
    def insert_recursive(self,data,node):
        if node.data > data:
            if node.leftChild == None:
                node.leftChild = TreeNode(data)
            else:
                self.insert_recursive(data,node.leftChild)
        else:
            if node.rightChild == None:
                node.rightChild = TreeNode(data)
            else:
                self.insert_recursive(data,node.rightChild)
    
    def inOrderTraversal(self,node,results = []):
        if node:
            self.inOrderTraversal(node.leftChild,results)
            results.append(node.data)
            self.inOrderTraversal(node.rightChild,results)
        return results
# Insertion Sort
def insertionSort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i - 1
        while j>=0 and key<array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key
# Selection Sort
def selectionSort(array):
    n = len(array)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1,n):
            if array[j] < array[minIndex]:
                minIndex = j
        array[i],array[minIndex] = array[minIndex],array[i]
# Linear Search
def linearSearch(array,target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1
# Binary Search
def BinarySearch(array,target,high,low):
    if high>=low:
        mid = (high+low)//2
        if array[mid] == target:
            return mid
        elif array[mid]>target:
            return BinarySearch(array,target,high-1,low)
        elif array[mid]<target:
            return BinarySearch(array,target,high,low+1)
    else:
        return -1
# Depth First Search
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdges(self,u,v):
        self.graph[u].append(v)
    
    def DFSUtils(self,v,visited):
        visited[v] = True
        print(v)
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtils(i,visited)
    def DFS(self):
        V = len(self.graph)
        visited = [False]*V
        for i in range(V):
            if visited[i] == False:
                self.DFSUtils(i,visited)
# Breadth First Search
visited = []
queue = []

def bfs(graph,node,visited):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m,end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Floyd Warshall Algorithm
nV = 4
INF = float('inf')

def floyd_warshall(G):
    distance = list(map(lambda i:list(map(lambda j:j,i)),G))
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j],distance[i][k]+distance[k][j])
    print_solution(distance)
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            print(distance[i][j],end=" ")
        print(" ")

# Evaluation of post fix expressionx
def evaluation(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            top = stack.pop()
            second = stack.pop()
            if char=="+":
                stack.append(second+top)
            elif char=='-':
                stack.append(second-top)
            elif char == 'x':
                stack.append(second*top)
            elif char == '/':
                stack.append(second//top)
            elif char=='%':
                stack.append(second%top)
            else:
                stack.append(second**top)
    return stack.pop()


treeValue  = [10,2,5,7,8]
tree = BinaryTree()
for i in treeValue:
    tree.insert(i,tree.root)
print(tree.inOrderTraversal(tree.root))

arrayOne = [5,3,21,8,10,1,4,2]
arrayTwo = arrayOne.copy()

print(linearSearch(arrayOne,10))

selectionSort(arrayOne)
insertionSort(arrayTwo)

print(BinarySearch(arrayTwo,10,len(arrayTwo)-1,0))

print(arrayOne)
print(arrayTwo)

G = [[0, 3, INF, 5], 
[2, 0, INF, 4], 
[INF, 1, 0, INF], 
[INF, INF, 2, 0]] 
floyd_warshall(G)

g = Graph()
g.addEdges(0,1)
g.addEdges(0,2)
g.addEdges(1,2)
g.addEdges(2,0)
g.addEdges(2,3)
g.addEdges(3,3)

print("Edge Traversal")

g.DFS()

graph = { 
'5' : ['3','7'], 
'3' : ['2', '4'], 
'7' : ['8'], 
'2' : [], 
'4' : ['8'], 
'8' : [] 
}
print("Breadth first search")
bfs(graph,'5',visited)