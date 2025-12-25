def isTwiceRepeated(num: str)-> bool:
    str_len = len(num)

    if str_len % 2 != 0:
        return False

    return num[0:str_len//2] == num[str_len//2:]

sum_repeated_ids = 0

with open("ids.txt", "r") as raw_ids:
    for ids in raw_ids.readline().split(","):
        split_ids = ids.split("-")

        for id in range(int(split_ids[0]), int(split_ids[1]) + 1):

            if isTwiceRepeated(str(id)):
                sum_repeated_ids += id

print(sum_repeated_ids)