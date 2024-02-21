class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.limit is None or len(self.items) < self.limit:
            self.items.append(item)
            return True  # Push successful
        else:
            return False  # Push unsuccessful, stack is full
        
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None  # Return None when attempting to pop from an empty stack

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None  # Return None when attempting to peek from an empty stack

    def size(self):
        return len(self.items)

    def full(self):
        return self.limit is not None and len(self.items) == self.limit

    def empty(self):
        return len(self.items) == 0

    def search(self, target):
        try:
            index = len(self.items) - self.items[::-1].index(target)
            return len(self.items) - index
        except ValueError:
            return -1
