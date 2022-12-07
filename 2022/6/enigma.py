# 🎄 Advent of Code 2022: Day 6 🎄  
# https://adventofcode.com/2022/day/6
 
data = open('../inputs/day6.txt').read()
print(f"Part 1 Solution: {[len(set(data[i:i+4]))for i in range(len(data))].index(4)+4}")
print(f"Part 2 Solution: {[len(set(data[i:i+14]))for i in range(len(data))].index(14)+14}")