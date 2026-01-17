class Row:
    def __init__(self, data: str):
        self.data = [*data.strip()]
        self.prev_row = None
        self.next_row = None

    def getAroundCountChar(self, index: int, char: str) -> int:

        if index < 0 or index >= len(self.data):
            raise BaseException("Invalid index ("+str(index)+") of len = " + str(len(self.data)))

        count = 0

        if self.prev_row is None and self.next_row is None:
            return count

        for row in [self.prev_row, self.next_row]:
            for i in (index - 1, index, index + 1):
                if row is not None:
                    count += int(row[i] == char)

        count += (self[index - 1] == char)
        count += (self[index + 1] == char)

        return count

    def withPrevRow(self, row):
        self.prev_row = row
        return self

    def withNextRow(self, row):
        self.next_row = row
        return self

    def __getitem__(self, key: int):
        """

        :param key:
        :return: str | None
        """

        if key < 0 or key >= len(self.data):
            return None

        return self.data[key]

    def __len__(self):
        return len(self.data)
