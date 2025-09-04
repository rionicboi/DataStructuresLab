class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        else:
            self.head.prev = newNode
            newNode.next = self.head
    
    def insertAtIndex(self, value, index):
        if index == 0:
            self.insertAtBeginning()
            return
        position = 0
        curr = self.head
        while curr != None and position + 1 != index:
            position += 1
            curr = curr.next
        if curr != None:
            newNode = Node(value)
            newNode.next = curr.next
            newNode.prev = curr
            curr.next.prev = newNode
            curr.next = newNode
        else:
            print("Index not found")

    def insertAtEnd(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode
        newNode.prev = curr
    
    def deleteFirstNode(self):
        if self.head is None:
            return
        self.head = self.head.next
    
    def deleteLastNode(self):
        if self.head is None:
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.prev.next = None

    def deleteFromIndex(self, index):
        if self.head is None:
            return
        if index == 0:
            self.deleteFirstNode()
            return
        position = 0
        curr = self.head
        while curr.next != None and position < index:
            position += 1
            curr = curr.next
        if curr == None or curr.next == None:
            print("Index not found")
        else:
            curr.prev.next = curr.next
    def printList(self):
        if self.head:
            curr = self.head
            while curr != None:
                print(curr.data, "->", end=" ")
                curr = curr.next
        else:
            print("List empty")

    def mergeAnotherList(self, LL):
        if self.head is None:
            return LL.head
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = LL.head
        LL.head.prev = curr
        

DLL = DoublyLinkedList()
DLL.insertAtBeginning(1)
DLL.insertAtEnd(2)
DLL.insertAtEnd(3)
DLL.insertAtEnd(4)
DLL.insertAtEnd(5)
print("After insertion: ")
DLL.printList()

print()
print("After inserting in the middle: ")
DLL.insertAtIndex(10, 3)
DLL.printList()

print()
print("Deleting first element: ")
DLL.deleteFirstNode()
DLL.printList()

print()
print("Deleting at end: ")
DLL.deleteLastNode()
DLL.printList()

print()
print("Deleting node 2: ")
DLL.deleteFromIndex(2)
DLL.printList()

DLL2 = DoublyLinkedList()
DLL2.insertAtBeginning(5)
DLL2.insertAtEnd(6)
DLL2.insertAtEnd(7)
DLL2.insertAtEnd(8)
DLL2.insertAtEnd(9)
print()
print("Second list: ")
DLL2.printList()

DLL.mergeAnotherList(DLL2)
print()
print("Merged list: ")
DLL.printList()