# Advent of Code 2023 - Day 7 https://adventofcode.com/2023/day/7/answer
# Author: Chris Correa 

from typing import List

def hand_strength(hand: str) -> str:
    """ Returns sortable alpha str representing strength of hand"""
    counts: dict[str, int] = {}
    
    for card in hand[0:5]:
        counts[card] = counts.get(card, 0) + 1

    if len(counts) == 1:
        return "A" # five of a kind
    elif len(counts) == 2:
        if 4 in counts.values():
            return "B" # four of a kind
        else:
            return "C" # full house
    elif len(counts) == 3 and 3 in counts.values():
            return "D"  # three of a kind
    elif len(counts) == 3:
            return "E" # two pair
    elif len(counts) == 4:
        return "F" # one pair
    else:
        return "G" # high card

CARD_MAP: dict[str,str] = {
    'A': 'A',
    'K': 'B',
    'Q': 'C',
    'J': 'D',
    'T': 'E',
    '9': 'F',
    '8': 'G',
    '7': 'H',
    '6': 'I',
    '5': 'V',
    '4': 'W',
    '3': 'X',
    '2': 'Y'
}   

P2_CARD_MAP: dict[str,str] = CARD_MAP.copy()
P2_CARD_MAP['J'] = 'Z' # For part two, J's are low card

def get_max_strength(hand: str) -> str:
    #if J's are wild...
    possibilities: list[str] = []
    for c in CARD_MAP.keys():
        possibilities.append(hand_strength(hand.replace("J", c))) 
    return min(possibilities)


def sortable_hand(hand: str, cardmap: dict) -> str:
    #convert A,K,Q,J,T,9,8,7... to (sortable) alpha values via cardmap
    return ''.join([cardmap[card] for card in hand])

def get_sum_of_bids(results: dict) -> list[int]:
    results = {k: v for k, v in sorted(results.items(), key=lambda item: item[0], reverse=True)}
    
    values: list[int] = []
    for idx, (key, val) in enumerate(results.items()):
        values.append(val * (idx+1))
    
    return sum(values)


# Part 1
def solve_part1(data: List[str]) -> int:
    strength: list[str] = [hand_strength(hand) for hand in data]
    bids: list[int] = [int(hand.split(" ")[1]) for hand in data]
    
    results: dict = {}
    for idx, hand in enumerate(data):
        #sortable hand endcoding
        hcode = f"{strength[idx]}-{sortable_hand(hand.split(' ')[0],CARD_MAP)}"
        results[hcode] = bids[idx]
    
    return get_sum_of_bids(results)
    
# Part 2
def solve_part2(data: List[str]) -> int:
    strength: list[str] = [get_max_strength(hand) for hand in data]
    bids: list[int] = [int(hand.split(" ")[1]) for hand in data]
    
    results: dict = {}
    for idx, hand in enumerate(data):
        #sortable hand endcoding
        hcode = f"{strength[idx]}-{sortable_hand(hand.split(' ')[0],P2_CARD_MAP)}"
        results[hcode] = bids[idx]
    
    return get_sum_of_bids(results)


# Main function
def main() -> None:
    # Read input file
    data: List[str] = open('./2023/inputs/day7.txt').read().splitlines()
    
    # Solve Part 1
    print(f"Part 1: {solve_part1(data)}")

    # Solve Part 2
    print(f"Part 2: {solve_part2(data)}")

if __name__ == "__main__":
    main()
