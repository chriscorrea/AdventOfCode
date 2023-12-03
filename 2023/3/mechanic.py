# Advent of Code 2023 - Day 3 https://adventofcode.com/2023/day/3
# Author: Chris Correa 

from typing import List
import re

def get_numbers(data: List[str]) -> List:
    results = []
    for idx,row in enumerate(data):
        # Use regex :( to find consecutive numeric sequences
        matches = re.finditer(r'\d+', row)
        for match in matches:
            results.append([idx,match.start(),int(match.group())])
    return results
   
def get_schematic(data: List[str]) -> List:
    """ Find all non-period symbols in the schematic"""
    symbols = set()
    for ridx, row in enumerate(data):
        for cidx, schematic in enumerate(row):
            if schematic.isalnum() is False and schematic != ".":
                #add the coordinates to the symbol set
                symbols.add((ridx, cidx))          
    return symbols

def get_gears(data: List[str]) -> List:
    """ Find all * ("gears") in the schematic"""
    gears = set()
    for ridx, row in enumerate(data):
        for cidx, schematic in enumerate(row):
            if schematic == "*":
                gears.add((ridx, cidx))          
    return gears

# Part 1
def solve_part1(data: List[str]) -> int:
    symbols = get_schematic(data)
    numbers = get_numbers(data)
    results = []
    for number in numbers:
        for symbol in symbols:
            if symbol[0] >= max(number[0]-1,0) and symbol[0] <= number[0]+1 and symbol[1] >= number[1]-1 and symbol[1] <= (number[1]+len(str(number[2]))):
                results.append(number[2])
                break
    return sum(results)

# Part 2
def solve_part2( data: List[str]) -> int:
    gears = get_gears(data)
    numbers = get_numbers(data)
    products = []
    for gear in gears:
        neighbors = []  
        for number in numbers:
            if gear[0] >= max(number[0]-1,0) and gear[0] <= number[0]+1 and gear[1] >= number[1]-1 and gear[1] <= (number[1]+len(str(number[2]))):
                neighbors.append(number)
        if len(neighbors) == 2:
            products.append(neighbors[0][2] * neighbors[1][2])

    return sum(products)

def main() -> None:
    # Read input file
    data: List[str] = open('./2023/inputs/day3.txt').read().splitlines()
    
    # Solve Part 1
    print(f"Part 1: {solve_part1(data)}")

    # Solve Part 2
    print(f"Part 2: {solve_part2(data)}")

if __name__ == "__main__":
    main()
