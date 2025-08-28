class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    #Insertion
    def insertAtBeginning(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
    
    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBeginning(data)
            return
        position = 0
        curr = self.head
        while curr != None and position + 1 != index:
            position += 1
            curr = curr.next
        if curr != None:
            newNode = Node(data)
            newNode.next = curr.next
            curr.next = newNode
        else:
            print("Index not found!")
        
    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode
    
    #Updation
    def updateNode(self, val, index):
        curr = self.head
        position = 0
        if position == index:
            curr.data = val
        else:
            while curr != None and position != index:
                position += 1
                curr = curr.next
            if curr != None:
                curr.data = val
            else:
                print("Index not available")
    
    #Deletion
    def delFirstNode(self):
        if self.head == None:
            return
        self.head = self.head.next
    
    def delLastNode(self):
        if self.head == None:
            return
        curr = self.head
        while curr.next != None and curr.next.next != None:
            curr = curr.next

        curr.next = None
    
    def delFromIndex(self, index):
        if self.head == None:
            return
        if index == 0:
            self.delFirstNode()
        
        position = 0
        curr = self.head
        while curr.next != None and position < index - 1:
            position += 1
            curr = curr.next
        if curr == None or curr.next == None:
            print("Index not found")
        else:
            curr.next = curr.next.next
    
    #print LinkedList
    def printList(self):
        if self.head:
            curr = self.head
            while curr.next != None:
                print(curr.data, "->", end=" ")
                curr = curr.next
        else:
            print("List empty")

    

#Working
LL = LinkedList()
LL.insertAtBeginning(1)
LL.insertAtEnd(2)
LL.insertAtEnd(3)
LL.insertAtEnd(4)
LL.insertAtEnd(5)
LL.insertAtEnd(6)
print("Current List: ")
LL.printList()

#insert at index
LL.insertAtIndex(10, 3)
print()
print("After inserting value: ")
LL.printList()

#Updating at index
LL.updateNode(15, 3)
print()
print("After updating node: ")
LL.printList()

#Deletion
LL.delFirstNode()
print()
print("Deleted first node: ")
LL.printList()

LL.delFromIndex(2)
print()
print("After deleting element at index 2: ")
LL.printList()

LL.delLastNode()
print()
print("After deleting last node: ")
LL.printList()