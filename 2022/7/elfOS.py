# 🎄📟 Advent of Code 2022: Day 7 📟🎄  
# https://adventofcode.com/2022/day/7

from collections import defaultdict
import re

def getDir(x,cwd):
    if x=="$ cd ..":
        location.pop()
        return location
    else:
        location.append(x[5:].strip())
        return location

data = open('../inputs/day7.txt').read()
location = [] 
files = defaultdict(int)

for x in data.splitlines():
    if x[0:4]=="$ cd":
        location = getDir(x,location)
    elif x[0:4]=="$ ls":   
        continue 
    else: # seek files / filesizes
        matches = re.finditer('(\d+)\s+([A-z\.\_]+)',x)
        for match in matches:
            fs = int(match.groups()[0])
            # Add fs value to all directories in tree
            for i in range(len(location)+1):
                files["/".join(location[:i])] += fs


# Part 1: All directories with total size < 100,000 
print(f"Part 1 Solution: {sum([v if v<100000 else 0 for k,v in files.items()])}")

# Part 2: Free up 3,000,0000 by deleting one directory
targetBytes = 30000000-(70000000 - sum([v if bool(re.search('\/\/[A-z]+$', k)) else 0 for k,v in files.items()]))
print(f"Part 2 Solution: {min([v if v>=targetBytes else 99999999 for k,v in files.items()])}")