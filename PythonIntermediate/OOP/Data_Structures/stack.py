#Data structures - Stack implementation

class Node:
    data : str
    next : 'Node'

    def __init__(self, data, next=None):
        self.data = data
        self.next = next



class Stack:
    head : Node

    def __init__(self, head):
        self.head = head

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if self.head is None:
            return None
        popped_node = self.head
        self.head = self.head.next
        return popped_node.data

    def print_structure(self):
        current_node = self.head
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

#example usage of the Stack class
print("\nCreating a stack with three nodes...\n")
first_node = Node("First", )
second_node = Node("Second", first_node)
third_node = Node("Third", second_node)

stack = Stack(third_node)
stack.print_structure()

print("\nPushing new data onto the stack...\n")

#example usage of the push
stack.push("Fourth")
stack.push("Fifth")
stack.print_structure()

print("\nPopping the last node to enter the stack..\n")

#example usage of the pop
popped_data = stack.pop()
stack.print_structure()