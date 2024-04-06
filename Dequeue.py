class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def append_right(self, item):
        self.items.append(item)

    def append_left(self, item):
        self.items.insert(0, item)

    def pop_right(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Deque is empty"

    def pop_left(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Deque is empty"

    def peek_right(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Deque is empty"

    def peek_left(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Deque is empty"

    def size(self):
        return len(self.items)

# Example usage:
deque = Deque()
print("Is the deque empty?", deque.is_empty())

deque.append_right(1)
deque.append_right(2)
deque.append_right(3)

print("Deque after appending to the right:", deque.items)
print("Right end of the deque:", deque.peek_right())

deque.append_left(0)
print("Deque after appending to the left:", deque.items)
print("Left end of the deque:", deque.peek_left())

popped_right = deque.pop_right()
print(f"Popped from the right end: {popped_right}")
popped_left = deque.pop_left()
print(f"Popped from the left end: {popped_left}")

print("Deque after popping from both ends:", deque.items)
print("Size of the deque:", deque.size())
