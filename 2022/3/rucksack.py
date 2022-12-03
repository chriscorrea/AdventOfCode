# 🎄 Advent of Code 2022: Day 3 🎄  
# https://adventofcode.com/2022/day/3

import os.path
import string
file = open(os.path.dirname(__file__) + '/../inputs/day3.txt')
data = file.read().split("\n")

#priority of each item is string position + 1
PRIORITY = string.ascii_lowercase + string.ascii_uppercase

#Part 1: Break rucksacks up into two compartments
rucksacks = list(map(lambda x: [x[:int(len(x)/2)], x[int(len(x)/2):]], data))

#Part 2: Build sets of three rucksacks per gang of elves
elfGangs = []
for i in range(0, len(data), 3): 
    elfGangs.append([data[i],data[i+1],data[i+2]])

def getPriority(item):
    return PRIORITY.rfind(item)+1

def identifyDuplicate(sack):
    for i, val in enumerate(str(sack[0])):
        if val in sack[1]:
            return val
    return None

def identifyBadge(gang):
    for i, val in enumerate(gang[0]):
        if val in gang[1] and val in gang[2]:
            return val

# generate part 1 results
priorityPerRucksack = [getPriority(identifyDuplicate(sack) )for sack in rucksacks]

# generate part 2 results
priorityPerGang = [getPriority(identifyBadge(gang) )for gang in elfGangs] 

print(f"Part 1 Result: {sum(priorityPerRucksack)}")
print(f"Part 2 Result: {sum(priorityPerGang)}")