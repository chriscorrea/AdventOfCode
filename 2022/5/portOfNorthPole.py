import re

def parseData(lines):
    stacks = parseCrates([val for i, val in enumerate(lines) if '[' in val])
    
    instructRegx = re.compile(r'move (?P<size>\d+) from (?P<from>\d+) to (?P<to>\d+)')

    instructions =  list(map(lambda row: {'size': int(row[0]),'from': int(row[1]),'to': int(row[2])}, [instructRegx.match(val).groups() for i, val in enumerate(lines) if 'to' in val]))
    return (stacks, instructions)

def parseCrates(crateStacks):
    results = [[],[],[],[],[],[],[],[],[],[]]
    for s in crateStacks:
        for i in range(1,34,4):
            if len(s)>i and s[i]!=" ":
                results[(i+3)//4].append(s[i]) 
    return(results)

def part1(crates,instructions):
    for move in instructions:
        cratesInMotion = list(crates[move['from']][0:move['size']])
        crates[move['to']] = list(reversed(cratesInMotion)) + crates[move['to']] 
        del crates[move['from']][0:move['size']]
    return [stack[0] for stack in crates[1:10]]

def part2(crates,instructions):
    for move in instructions:
        cratesInMotion = list(crates[move['from']][0:move['size']])
        crates[move['to']] = list((cratesInMotion)) + crates[move['to']] 
        del crates[move['from']][0:move['size']]
    return [stack[0] for stack in crates[1:10]]

#data = open('../inputs/day5.test.txt').read().splitlines()
data = open('../inputs/day5.txt').read().splitlines()


crates, instructions = parseData(data)
print(f"Part 1 Result: {part1(crates,instructions)}")

crates, instructions = parseData(data)
print(f"Part 2 Result: {part2(crates,instructions)}")