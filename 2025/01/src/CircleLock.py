from .RingBuffer import RingBuffer

class CircleLock:

    def __init__(self, start_digit: int, end_digit: int):
        self.ring_buffer = RingBuffer(start_digit, end_digit)

    def getValue(self):
        return self.ring_buffer.getValue()

    def rotate(self, direction: str, steps=0):
        """
        rotate lock on n steps through direction
        :param direction: 'L'|'R' -- left or right direction (prev or next) or in format 'L<int>' | 'R<int>'
        :param steps:
        :return: self
        """

        if steps == 0 and len(direction) <= 1:
            raise "invalid rotation format"

        if steps == 0:
            steps = int(direction[1:])
            direction = direction[0]

        if direction.upper() == 'L':
            self.ring_buffer.iteratePrev(steps)
        elif direction.upper() == 'R':
            self.ring_buffer.iterateNext(steps)
        else:
            raise "Invalid direction rotate"

        return self

    def withReachValue(self, value: int):
        self.ring_buffer.setSearchReachesValue(value)

    def getCountReachedValue(self) -> int:
        return self.ring_buffer.getCountIntersectReachedValue()