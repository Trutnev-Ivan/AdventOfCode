from .Node import Node

class RingBuffer:
    def __init__(self, start_digit: int, end_digit: int):
        if end_digit - start_digit < 1:
            raise "Count buffer must be >= 1"

        self.current = Node(start_digit)
        next_node = None
        prev_node = self.current

        for i in range(start_digit + 1, end_digit+1):
            next_node = Node(i, None, prev_node)
            prev_node.setNext(next_node)
            prev_node = next_node

        self.current.setPrev(prev_node)
        prev_node.setNext(self.current)

    def getValue(self):
        return self.current.getValue()

    def iteratePrev(self, n: int):
        for i in range(n):
            self.current = self.current.prev()

    def iterateNext(self, n: int):
        for i in range(n):
            self.current = self.current.next()