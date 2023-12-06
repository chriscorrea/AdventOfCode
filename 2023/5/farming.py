# Advent of Code 2023 - Day 5 https://adventofcode.com/2023/day/5
# Author: Chris Correa 

from typing import List
import re
import json

def get_values(data: str) -> dict:
    pattern = r'([\w\s\-]+):\s?([\d\s]+)' 
    matches = re.findall(pattern, data)
    result: dict = {key: [x.strip().split(" ") for x in str(value).split("\n") if len(x)>1] for key, value in matches}
    #iterate through  items in result
    return result



# Part 1
def solve_part1(data: List[str]) -> int:
    farm_map: str = '\n'.join(data)
    codex: dict = get_values(farm_map)
    print(codex)

    results: dict = {}
    for seed in codex['seeds'][0]:
        target: int = seed
        for conversion in codex.keys():
            if conversion != 'seeds':
                updated: bool = False
                for recipe in codex[conversion]:
                    if updated is False:
                        if int(target) in range(int(recipe[1]), int(recipe[1])+int(recipe[2])):
                            updated = True
                            target = int(recipe[0])+int(target)-int(recipe[1])
                            
        results[seed] = target  
    return min(results.values())

# Part 2
def solve_part2(data: List[str]) -> int:
    # TODO: Implement your solution for Part 2

    pass


# Main function
def main() -> None:
    # Read input file
    data: List[str] = open('./2023/inputs/day5.txt').read().splitlines()
    
    # Solve Part 1
    print(f"Part 1: {solve_part1(data)}")

    # Solve Part 2
    print(f"Part 2: {solve_part2(data)}")

if __name__ == "__main__":
    main()
