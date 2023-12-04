# Advent of Code 2023 - Day 4 
# Author: Chris Correa 

from typing import List
import math

def get_card_score(card: str) -> int:
    """"
    Returns int: raw score (number of winning number matches)
    """
    score = 0
    winners = [int(w) for w in card.split(":")[1].split('|')[0].strip().split(" ") if w != '' ]
    candidates = [int(c) for c in card.split(":")[1].split('|')[1].strip().split(" ") if c != '']
    for c in candidates:
        if c in winners:
            score += 1
    return score

# Part 1
def solve_part1(data: List[str]) -> int:
    # get sum of card scores for each line
    total_scores = []
    for card in data:
        score = get_card_score(card)
        total_scores.append(score if score < 3 else pow(2,score-1))
    return sum(total_scores)

# Part 2
def solve_part2(data: List[str]) -> int:
    # initiate card totals list
    card_totals = [1 for card in data]
    # iterate through each card to estimate new card totals
    for idx, card in enumerate(data):
        score = get_card_score(card)
        for _ in range(0, card_totals[idx]):
            for i in range(1, score+1):
                card_totals[idx+i] += 1
    return sum(card_totals)

# Main function
def main() -> None:
    # Read input file
    data: List[str] = open('./2023/inputs/day4.txt').read().splitlines()
    
    # Solve Part 1
    print(f"Part 1: {solve_part1(data)}")

    # Solve Part 2
    print(f"Part 2: {solve_part2(data)}")

if __name__ == "__main__":
    main()