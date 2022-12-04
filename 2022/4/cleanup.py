# 🎄 Advent of Code 2022: Day 4 🎄  
# https://adventofcode.com/2022/day/4

data = open('../inputs/day4.txt').read().splitlines()

def overlap(assignment):
    sites = [set(range(int(a.split('-')[0]),int(a.split('-')[1])+1)) for a in assignment.split(",")]
    if len(sites[0].intersection(sites[1])) in [len(sites[0]),len(sites[1])]:
        return True
    else:
        return False

def anyOverlap(assignment):
    sites = [set(range(int(a.split('-')[0]),int(a.split('-')[1])+1)) for a in assignment.split(",")]
    if len(sites[0].intersection(sites[1]))>0:
        return True
    else:
        return False

print(f"Part 1 Result: {sum( [overlap(assignment)for assignment in data] )}")
print(f"Part 2 Result: {sum( [anyOverlap(assignment)for assignment in data] )}")