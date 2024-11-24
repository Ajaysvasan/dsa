class Node:
    def __init__(self,coeff,pow):
        self.pow = pow
        self.coeff = coeff
        self.next = None

class PolynomialAddition:
    def add(self,listOne,listTwo):
        head = Node(0,0)
        current = head
        while listOne and listTwo:
            if listOne.pow == listTwo.pow:
                current.next = Node(listOne.coeff+listTwo.coeff,listTwo.pow)
                current,listOne,listTwo = current.next,listOne.next,listTwo.next

            elif listOne.pow > listTwo.pow:
                current.next = Node(listOne.coeff,listOne.pow)
                current,listOne = current.next,listOne.next

            else:
                current.next = Node(listTwo.coeff,listTwo.pow)
                current,listTwo = current.next,listTwo.next
        return head.next
def createPolynomial(coeffs,powers):
    head = None
    current = None
    for coeff,pow in zip(coeffs,powers):
        newnode = Node(coeff,pow)
        if not head:
            head = newnode
            current = newnode
        else:
            current.next = newnode
            current = current.next
    return head
def printPoly(poly):
    result = []
    while poly:
        result.append(f'{poly.coeff}^{poly.pow}')
        poly = poly.next

    print(" + ".join(result))

list1_coeff = [5,2,1]
list1_power = [3,2,1]

list2_coeff = [3,2,1]
list2_power = [3,2,0]

listOne = createPolynomial(list1_coeff,list1_power)
listTwo = createPolynomial(list2_coeff,list2_power)

poly = PolynomialAddition()
listThree = poly.add(listOne,listTwo)

printPoly(listThree)