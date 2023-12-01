# Advent of Code 2023 - Day 1 @ https://adventofcode.com/2023/day/1
# Author: Chris Correa 

from functools import reduce
from typing import List

# Part1
def solve_part1(data: List[str]) -> int:
    # declutter string by removing all non-numeric characters
    decluttered = ["".join(filter(lambda x: x.isnumeric(), value)) for value in data]
    # get the first and last character of each list element
    cleaned = [int(value.strip()[0]+value.strip()[-1]) for value in decluttered if len(value) > 0]
    # return the sum of the list
    print(len(cleaned))
    return reduce(lambda x, y: x + y, cleaned)

# translating 'two' to 't2o' to work around cases such as 'twone'
TRANSLATOR = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}

# Part2
def solve_part2(data: List[str]) -> int:
    # we are going to translate words into numbers
    translated = []

    for datum in data:
        # replace all number words with their numeric equivalent
        for key,val in TRANSLATOR.items():
            datum = datum.replace(key, str(val)).strip() if key in datum else datum
        # store new string to translated list
        translated.append(datum)
    
    return solve_part1(translated)

# Main function
def main() -> None:
    # Read input file
    data = open('../inputs/day1.txt').read().splitlines()
    
    # Solve Part 1
    result_part1 = solve_part1(data)
    print("Part 1:", result_part1)

    # Solve Part 2
    result_part2 = solve_part2(data)
    print("Part 2:", result_part2)

if __name__ == "__main__":
    main()
