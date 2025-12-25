from src.CircleLock import CircleLock


lock = CircleLock(0, 99)
lock.rotate("R50")

with open("rotate.txt", "r") as rotate_file:
      rotate_rule = rotate_file.readline()
      count_zeros = 0

      while rotate_rule:
            rotate_rule = rotate_rule.rstrip("\n")

            if lock.rotate(rotate_rule).getValue() == 0:
                  count_zeros += 1

            rotate_rule = rotate_file.readline()


      print(count_zeros)