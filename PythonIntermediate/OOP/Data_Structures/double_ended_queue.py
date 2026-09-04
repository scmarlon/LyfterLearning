class Node:
    data : str
    next : 'Node'

    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class DoubleEndedQueue:
    head : Node
    tail : Node

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

        if self.head is not None and self.tail is None:
            self.tail = self.head
    
    def push_right(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def push_left(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def pop_right(self):
        if self.tail is None:
            return None
        popped_node = self.tail
        self.tail = self.tail.previous
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None  # If the queue becomes empty
        return popped_node.data
    
    def pop_left(self):
        if self.head is None:
            return None
        popped_node = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.previous = None
        else:
            self.tail = None  # If the queue becomes empty
        return popped_node.data

    def print_right(self):
        current_node = self.tail
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def print_left(self):
        current_node = self.head
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def print_structure(self):
        print("Double-ended queue structure:")
        current_node = self.head
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

#example usage of the DoubleEndedQueue class
print("\nCreating a double-ended queue nodes...\n")
first_node = Node("First")

double_queue = DoubleEndedQueue(first_node)


double_queue.push_right("Second, right")
double_queue.push_right("Third, right")

double_queue.print_structure()
print("------------")

double_queue.push_left("Fourth, left")
double_queue.push_left("Fifth, left")

double_queue.print_structure()

print("------------")

print("Popping from the right...")

popped_data_right = double_queue.pop_right()
print(f"Popped data from right: {popped_data_right}")

double_queue.print_structure()

print("------------")

popped_data_left = double_queue.pop_left()
print(f"Popped data from left: {popped_data_left}")

double_queue.print_structure()