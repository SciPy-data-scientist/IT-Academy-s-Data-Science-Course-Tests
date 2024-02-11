class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, last_value):
        new_node = Node(last_value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def unshift(self, first_value):
        new_node = Node(first_value)
        if self.head is None:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node = self.head
    
    def pop(self):
        if self.head is None:
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node = None

    def shift(self):
        if self.head is None:
            return
        first_node = self.head
        if first_node.next is None:
            first_node = None
        first_node.next = self.head
        first_node = None
