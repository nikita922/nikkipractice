class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty"

    def size(self):
        return len(self.items)

# Example usage:
queue = Queue()
print("Is the queue empty?", queue.is_empty())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue after enqueuing 1, 2, and 3:", queue.items)
print("Front of the queue:", queue.peek())

dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)
print("Queue size:", queue.size())
