# Advent of Code 2023 - Day 6 https://adventofcode.com/2023/day/6 
# Author: Chris Correa 

from typing import List
import math

# Part 1
def solve(data: List[str]) -> int:
    winners: list[int] = []
    for i in range(len(data['time'])):
        race: list[int] = []
        t, d = int(data['time'][i]), int(data['distance'][i])
        for j in range(1,t):
            dist = (j)*(t-j)
            #print(f"{j} travels {dist}")
            if dist > d:
                race.append(j)
        winners.append(len(race))
    return(math.prod(winners))

# Main function
def main() -> None:
    # Read input file
    data: List[str] = open('./2023/inputs/day6.txt').read().splitlines()
    
    race_data = {
        'time': [int(x.strip()) for x in data[0].split(": ")[1].split(" ") if len(x)>0],
        'distance': [int(x.strip()) for x in data[1].split(": ")[1].split(" ") if len(x)>0], 
    }

    kerning_adjusted_data = {
        'time':     [data[0].split(": ")[1].replace(" ","")],
        'distance': [data[1].split(": ")[1].replace(" ","")]
    } 
    
    # Solve Part 1
    print(f"Part 1: {solve(race_data)}")

    # Solve Part 2 with brute force :/
    print(f"Part 2: {solve(kerning_adjusted_data)}")

if __name__ == "__main__":
    main()
