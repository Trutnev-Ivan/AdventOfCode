from .Row import Row

class RollFinder:
    def __init__(self, less_count_rolls_around: int, roll_char="@"):

        if less_count_rolls_around <= 1:
            raise BaseException("Count rolls around must be >= 1")

        self.less_count_rolls_around = less_count_rolls_around
        self.roll_char = roll_char

    def findByFile(self, path: str) -> int:
        count = 0

        with open(path, "r") as file:

            rows = self._initRows(file)

            if len(rows) == 0:
                return count

            for i in range(len(rows[1])):
                if rows[1][i] != self.roll_char:
                    continue

                count += int(rows[1].getAroundCountChar(i, self.roll_char) < self.less_count_rolls_around)

            row = file.readline()

            while len(row) > 0:
                rows[0] = rows[1]
                rows[1] = rows[2]
                rows[2] = Row(row)

                rows[0].withNextRow(rows[1])
                rows[0].withPrevRow(None)

                rows[1].withNextRow(rows[2])
                rows[1].withPrevRow(rows[0])

                rows[2].withNextRow(None)
                rows[2].withPrevRow(rows[1])

                for i in range(len(rows[1])):
                    if rows[1][i] != self.roll_char:
                        continue

                    count += int(rows[1].getAroundCountChar(i, self.roll_char) < self.less_count_rolls_around)

                row = file.readline()

            # last row
            for i in range(len(rows[2])):
                if rows[2][i] != self.roll_char:
                    continue

                count += int(rows[2].getAroundCountChar(i, self.roll_char) < self.less_count_rolls_around)

        return count

    def _initRows(self, file) -> list:
        rows = [
            None,
            None,
            None
        ]

        row = file.readline()

        if len(row) == 0:
            return []

        rows[1] = Row(row)
        row = file.readline()

        if len(row) == 0:
            return rows

        rows[2] = Row(row)

        rows[1].withNextRow(rows[2])
        rows[2].withPrevRow(rows[1])

        return rows
