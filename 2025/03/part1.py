def getJoltage(battery: str) -> int:
    indexes = []
    first_digit = 0
    second_digit = 0

    for i in range(len(battery) - 1):

        c = battery[i]

        if int(c) > first_digit:
            first_digit = int(c)
            indexes = []

        if int(c) == first_digit:
            indexes.append(i)

    for i in indexes:
        for c in battery[i+1:]:
            if int(c) > second_digit:
                second_digit = int(c)

    return first_digit*10 + second_digit


sum = 0

with open("batteries.txt", "r") as batteries_file:
    battery = batteries_file.readline()

    while battery:
        battery = battery.rstrip("\n")
        sum += getJoltage(battery)
        battery = batteries_file.readline()

print(sum)