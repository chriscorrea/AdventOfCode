# https://adventofcode.com/2022/day/2
import os.path
import string
file = open(os.path.dirname(__file__) + '/../inputs/day3.txt')
data = file.read().split("\n")

#priority of each item is string position + 1
PRIORITY = string.ascii_lowercase + string.ascii_uppercase

#break rucksacks up into two compartments
rucksacks = list(map(lambda x: [x[:int(len(x)/2)], x[int(len(x)/2):]], data))

def getPriority(item):
    return PRIORITY.rfind(item)+1

def identifyDuplicate(sack):
    for i, val in enumerate(str(sack[0])):
        pass
        if val in sack[1]:
            return val
    return None

#part 1 results
priorityPerRucksack = [getPriority(identifyDuplicate(sack) )for sack in rucksacks]


print(f"Part 1 Result: {sum(priorityPerRucksack)}")
