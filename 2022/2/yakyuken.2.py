import os.path

# https://adventofcode.com/2022/day/2

file = open(os.path.dirname(__file__) + '/../inputs/day2.txt')
rounds = file.read().split("\n")

base_value = {'A':1,'B':2,'C':3}

# list of possible values is [1,2,3]
# Winning values will be initial + 1 % 2
# Losing values will be initial - 1 % 2
values = [1,2,3]

def score(round):
    play = round.split(" ")
    if play[1]=='Z':
        #win
        return values[(base_value[play[0]]+1) %len(values)-1] + 6
    elif play[1]=='Y':
        # draw
        return base_value[play[0]] + 3
    else:
        #loss
        return values[(base_value[play[0]]-1) %len(values)-1]

scores = list(map(score, rounds))
print(sum(scores))