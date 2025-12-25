def getJoltage(battery: str) -> int:
    count_digits = 12
    digits = []
    index = -1
    str_len = len(battery)

    while len(digits) < count_digits:
        digit = 0

        for i in range(index + 1, str_len):

            if int(battery[i]) > digit:
                digit = int(battery[i])
                index = i

            if str_len - i <= count_digits - len(digits):
                break

        digits.append(digit)

    joltage = 0
    for i in range(len(digits)):
        joltage += digits[i] * 10 ** (count_digits - i - 1)

    return joltage


sum = 0

with open("batteries.txt", "r") as batteries_file:
    battery = batteries_file.readline()

    while battery:
        battery = battery.rstrip("\n")
        sum += getJoltage(battery)
        battery = batteries_file.readline()

print(sum)