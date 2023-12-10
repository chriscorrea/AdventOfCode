# Advent of Code 2023 - Day 10 https://adventofcode.com/2023/day/10
# Author: Chris Correa 

from typing import List

#hard-coding 'S' starting position
START: tuple = (107,110)

MOVE: dict[str,tuple] = {
    "N": (-1, 0),
    "S": (1, 0),
    "W": (0, -1),
    "E": (0, 1),
}

PIPES: dict[str,list] = {
    "|": ["N", "S"],
    "L": ["N", "E"],
    "J": ["N", "W"],
    "-": ["W", "E"],
    "F": ["S", "E"],
    "7": ["S", "W"],
    'S': ["N","E","S","W"],
}

# Part 1
def solve_part1(data: List[str]) -> int:
    mapped: dict = {}
    search: list = [(START, 0)]
    
    while len(search) > 0:
        loc, steps = search.pop(0)
        if loc in mapped:
            continue #skip if already mapped
        mapped[loc] = steps
        for direction in PIPES[data[loc[0]][loc[1]]]:
            from_direction = "E" if direction=="W" else "W" if direction=="E" else "S" if direction=="N" else "N"
            xi, xj = MOVE[direction]
            target = (loc[0] + xi, loc[1] + xj)
            if loc[1] + xj < 0 or loc[1] + xj >= len(data[loc[0] + xi]):
                continue
            if loc[0] + xi < 0 or loc[0] + xi >= len(data):
                continue
            if data[loc[0] + xi][loc[1] + xj] not in PIPES:
                continue
            target_directions = PIPES[data[loc[0] + xi][loc[1] + xj]]
            if from_direction in target_directions:
                search.append((target, steps + 1))

    return max(mapped.values()) 

# Part 2
def solve_part2(data: List[str]) -> int:
    pass

# Main function
def main() -> None:
    # Read input file
    data: List[str] = open('./2023/inputs/day10.txt').read().splitlines()
    labirinto = [list(x) for x in data]

    # Solve Part 1 (6968)
    print(f"Part 1: {solve_part1(labirinto)}")

    # Solve Part 2
    print(f"Part 2: {solve_part2(data)}")

if __name__ == "__main__":
    main()
