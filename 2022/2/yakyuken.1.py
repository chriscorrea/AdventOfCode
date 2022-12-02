import os.path

# https://adventofcode.com/2022/day/2

file = open(os.path.dirname(__file__) + '/../inputs/day2.txt')
rounds = file.read().split("\n")

value_map = {'A':1,'B':2,'C':3,'X':1,'Y':2,'Z':3}

def score(round):
    play = round.split(" ")
    print(play)
    if value_map[play[0]] == value_map[play[1]]:
        # three additional points for a draw
        return value_map[play[1]]+3
    elif (value_map[play[1]]- value_map[play[0]]) in [1,-2]:
        # six additional points for a win
        return value_map[play[1]]+6
    else:
        # zero additional points for the loss
        return value_map[play[1]] 

scores = list(map(score, rounds))
print(sum(scores))
