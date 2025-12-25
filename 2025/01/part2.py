from src.CircleLock import CircleLock


lock = CircleLock(0, 99)
lock.rotate("R50")

with open("rotate.txt", "r") as rotate_file:
    lock.withReachValue(0)
    reached_zeros = 0

    rotate_rule = rotate_file.readline()

    while rotate_rule:
        rotate_rule = rotate_rule.rstrip("\n")
        reached_zeros += lock.rotate(rotate_rule).getCountReachedValue()
        rotate_rule = rotate_file.readline()

    print(reached_zeros)