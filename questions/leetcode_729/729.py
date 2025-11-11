class Node:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left = self.right = None

class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start, end):
        def insert(node, start, end):
            if not node:
                return Node(start, end), True
            if end <= node.start:
                node.left, ok = insert(node.left, start, end)
            elif start >= node.end:
                node.right, ok = insert(node.right, start, end)
            else:
                return node, False  
            return node, ok
        self.root, ok = insert(self.root, start, end)
        return ok
