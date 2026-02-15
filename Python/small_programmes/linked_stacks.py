class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # Points to the top node of the stack

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top  # New node points to current top
        self.top = new_node       # Top is now the new node

    def pop(self):
        if self.top is None:
            return None
        popped_item = self.top.data
        self.top = self.top.next  # Move top to next node
        return popped_item

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

# Example usage
stack = Stack()
stack.push('A')
stack.push('B')
stack.push('C')
print(stack.pop())  # Output: 'C'
print(stack.peek()) # Output: 'B'