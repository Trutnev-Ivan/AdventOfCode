from src.RollFinder import RollFinder

roll_finder = RollFinder(4, "@")
count_rolls = roll_finder.findByFile("rolls.txt")

print(count_rolls)
