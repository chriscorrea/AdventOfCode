# Advent of Code 2023 - Day 2 https://adventofcode.com/2023/day/2
# Author: Chris Correa 

from typing import List
from functools import reduce

def validate(game: str) -> bool:
    # returns True if game is valid given stated max cubes of each color
    for pull in game:
        for cube in pull:
            if int(cube[0]) > {'red': 12, 'blue': 14, 'green': 13}[cube[1]]:
                return False
    return True

def min_cubes(game: str) -> int:
    # returns the minimum number of cubes required to play the game
    cubes = {'red': 0, 'blue': 0, 'green': 0}
    for pull in game:
        for cube in pull:
            #print(cube)
            if int(cube[0]) > int(cubes[cube[1]]):
                #print("new min!")
                cubes[cube[1]] = int(cube[0])
    return cubes

def solve_part1(data: List[str]) -> int:
    """
        Returns an int representing the sum of valid game IDs.
    """
    valid = set()
    for game in data:
        id, pulls = game.strip().split(": ")
        pulls = [[cube.strip().split(" ") for cube in pull.strip().split(",")] for pull in pulls.split(";")]
        id = int(id.split(" ")[1].strip())
        if validate(pulls) is True:
            valid.add(id)

    return reduce(lambda x, y: x + y, valid)
    
def solve_part2(data: List[str]) -> int:
    """
        Returns an int representing the sum of power of minimum viable cubes per game.
    """
    powers = []
    for game in data:
        id, pulls = game.strip().split(": ")
        pulls = [[cube.strip().split(" ") for cube in pull.strip().split(",")] for pull in pulls.split(";")]
        id = int(id.split(" ")[1].strip())
        minimums = min_cubes(pulls)
        min_power = int(minimums['red']) * int(minimums['blue']) * int(minimums['green'])
        powers.append(min_power)
       
    return reduce(lambda x, y: x + y, powers)

# Main function
def main() -> None:
    # Read input file
    data: List[str] = open('../inputs/day2.txt').read().splitlines()
    
    print(f"Part 1: {solve_part1(data)}")

    print(f"Part 2: {solve_part2(data)}")

if __name__ == "__main__":
    main()
