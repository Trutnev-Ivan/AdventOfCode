def hasRepeatedNums(num: str)-> bool:
    str_len = len(num)

    if str_len <= 1:
        return False

    for sublen in range(1, str_len // 2 + 1):
        if str_len % sublen != 0:
            continue

        value = num[:sublen]
        is_all_parts_equals = True

        for i in range(1, str_len // sublen):
            is_all_parts_equals = is_all_parts_equals and value == num[i * sublen : (i+1)*sublen]

        if is_all_parts_equals:
            return True

    return False

sum_repeated_ids = 0

with open("ids.txt", "r") as raw_ids:
    for ids in raw_ids.readline().split(","):
        split_ids = ids.split("-")

        for id in range(int(split_ids[0]), int(split_ids[1]) + 1):
            if hasRepeatedNums(str(id)):
                sum_repeated_ids += id

print(sum_repeated_ids)