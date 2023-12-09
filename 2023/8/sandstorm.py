# Advent of Code 2023 - Day 8 https://adventofcode.com/2023/day/8
# Author: Chris Correa 

from typing import List
from itertools import cycle
from math import lcm 

# Part 1
def solve_part1(instructions, coords) -> int:
    step: int = 0
    idx: str = 'AAA'
    looped_instructions = cycle(instructions)
    while(True):
        step += 1
        instruct = next(looped_instructions)
        idx = coords[idx][instruct]
        if idx == 'ZZZ':
            return step

# Part 2
def solve_part2(instructions, coords, acoords) -> int:
    # As it happens, each ..A only reaches one ..Z per cycle. 
    # So we can find the cycle length for each starting point
    # and find the answer via least common multiple

    results: dict = {}

    for a in acoords:
        steps: int = 0
        idx: str = a
        looped_instructions = cycle(instructions)
        while idx.endswith('Z') == False:
            instruct = next(looped_instructions)
            idx = coords[idx][instruct] 
            steps += 1
        results[a] = steps

    # Find the least common multiple of all cycle lengths
    convergence: int = lcm(*list(results.values()))
    return convergence

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
