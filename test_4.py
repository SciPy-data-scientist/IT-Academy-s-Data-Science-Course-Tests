class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class DoubleLinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def push(self, value):
        """ Add a node to the end of the list """

        last_node = Node(value)

        if self.head is None: # List is empty
            self.head = last_node
            self.tail = self.head # The head is equal to the tail == last_node
            return
        
        self.tail.next = last_node # Assign the "next" link of the tail to the "last_node"
        last_node.prev = self.tail # Assign the "prev" link of the "last_node" to the tail
        self.tail = last_node # Move the tail to the current position of the "last_node"

    def unshift(self, value):
        """ Add a node to the beginning of the list """

        first_node = Node(value)

        if self.head is None: # List is empty
            self.head = first_node
            self.tail = self.head # The head is equal to the tail == first_node
            return
        
        self.head.prev = first_node # Assign the "prev" link of the head to the "first_node"
        first_node.next = self.head # Assign the "next" link of the "first_node" to the head
        self.head = first_node # Move the head to the current position of the "first_node"
    
    def pop(self):
        """ Delete a node from the end of the list """

        if self.head is None: # List is empty
            return
        elif self.head == self.tail: # List contains only one node
            self.head = None
            self.tail = None
            return
        else:    
            pointer = self.tail.prev # Assign a "pointer" to the previous node before the tail
            pointer.next = None # Assign a "next" link of the pointer to None
            self.tail = pointer # Assign a tail to the current position of the pointer

    def shift(self):
        """ Delete a node from the beginning of the list """

        if self.head is None: # List is empty
            return
        elif self.head == self.tail: # List contains only one node
            self.head = None
            self.tail = None
            return
        else:
            pointer = self.head.next # Assign a "pointer" to the next node after the head
            pointer.prev = None # Assign a "prev" link of the pointer to None
            self.head = pointer # Assign a head to the current position of the pointer

