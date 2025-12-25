from .Node import Node

class RingBuffer:
    def __init__(self, start_digit: int, end_digit: int):
        if end_digit - start_digit < 1:
            raise "Count buffer must be >= 1"

        self.reach_value = 0
        self.count_intersects_reached_value = 0
        self.current = Node(start_digit)
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
        self.count_intersects_reached_value = 0

        for i in range(n):
            self.current = self.current.prev()

            if self.current.getValue() == self.reach_value:
                self.count_intersects_reached_value += 1

    def iterateNext(self, n: int):
        self.count_intersects_reached_value = 0

        for i in range(n):
            self.current = self.current.next()

            if self.current.getValue() == self.reach_value:
                self.count_intersects_reached_value += 1

    def setSearchReachesValue(self, value: int):
        self.reach_value = value

    def getCountIntersectReachedValue(self) -> int:
        return self.count_intersects_reached_value