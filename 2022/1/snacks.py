from functools import reduce

file = open('day1.txt')
data = file.read()

#create list of elves, each item containing string of snack values
elves = data.split('\n\n')

#reduce function
def sum_snacks(first, second):
    return first+int(second if str(second).isdigit() else 0)

#create list of calorie totals
calories = [reduce(sum_snacks,elf.split('\n'),0) for elf in elves]

#part 1: sort list (ascending) and print final value
print(sorted(calories)[-1])

print(sorted(calories ))
#part 2: get top three values and sum:
print(reduce(sum_snacks,sorted(calories)[-3:],0))