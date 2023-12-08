# Advent of Code 2023 - Day 
# Author: Chris Correa 

from typing import List
from itertools import cycle

# Part 1
def solve_part1(instructions, coords) -> int:
    # TODO
    step: int = 0
    idx: str = 'AAA'
    looped_instructions = cycle(instructions)
    while(True):
        step += 1
        instruct = next(looped_instructions)
        print(f"{step}: {idx} then {instruct}")
        idx = coords[idx][instruct]
        if idx == 'ZZZ':
            return step
        

# Part 2
def solve_part2(instructions, coords, acoords) -> int:
    results: dict = {}

    for a in acoords:
        print('### ' + a)
        idx: str = a
        looped_instructions = cycle(instructions)
        results[a] = []

        for i in range(100000): #arbitrary - surely this won't work 
            instruct = next(looped_instructions)
            idx = coords[idx][instruct] 
            if idx.endswith('Z'):
                results[a].append(i)
  
    counts = {}
    for k in results.keys():
        for v in results[k]:
            counts[v] = counts.get(v, 0) + 1
    for k,v in counts.items():
        if v==len(acoords):
            return k
    
    return None

# Main function
def main() -> None:
    # Read input file
    data: List[str] = open('./2023/inputs/day8.txt').read().splitlines()

    # build list of left/right (0,1) instructions
    instructions: List[int] = [int(x.replace('L','0').replace('R','1')) for x in data[0]]

    #build dictionary of coordinates
    coords: dict = {}
    for row in data[2:]:
        k, v = row.split("=")
        vals = v.replace('(','').replace(')','').replace(' ','').split(',')
        coords[k.strip()] = tuple(vals)
    
    # Solve Part 1
    print(f"Part 1: {solve_part1(instructions,coords)}")

    #for part 2, need all keys ending with A
    acoords: list[str] = []
    for k in coords.keys():
        if k.endswith('A'):
            acoords.append(k)
    
    # Solve Part 2
    print(f"Part 2: {solve_part2(instructions,coords,acoords)}")

if __name__ == "__main__":
    main()
