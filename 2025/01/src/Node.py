class Node:

    def __init__(self, value: int, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def getValue(self) -> int:
        return self.value

    def next(self):
        return self.next_node

    def prev(self):
        return self.prev_node

    def setNext(self, node):
        self.next_node = node

    def setPrev(self, node):
        self.prev_node = node