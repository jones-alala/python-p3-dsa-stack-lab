class Stack:
    def __init__(self, items=None, max_size=None):
        self.items = items if items else []
        self.max_size = max_size

    def push(self, item):
        if self.max_size is None or len(self.items) < self.max_size:
            self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def full(self):
        return self.max_size is not None and len(self.items) >= self.max_size

    def search(self, target):
        """
        Search from top of the stack (right to left), return 0-based index
        e.g., top element = index 0
        """
        for i in range(1, len(self.items)+1):
            if self.items[-i] == target:
                return i - 1
        return -1
