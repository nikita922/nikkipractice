class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()

print("Is the stack empty?", stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack after pushing 1, 2, and 3:", stack.items)
print("Top of the stack:", stack.peek())
popped_item = stack.pop()
print(f"Popped item: {popped_item}")
print("Stack after popping:", stack.items)
print("Size of the stack:", stack.size())
