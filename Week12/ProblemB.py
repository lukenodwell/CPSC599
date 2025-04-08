from collections import defaultdict


def solve(choices, letters, starting_letter):
    for choice in choices:
        if choice[-1] == starting_letter and letters[choice[-1]] == 1:
            return choice + "!"
        elif letters[choice[-1]] == 0:
            return choice + "!"

    if choices:
        return choices[0]
    else:
        return "?"


starting_letter = input()[-1]
acount = int(input())

letters = defaultdict(lambda: 0)

animals = []
for _ in range(acount):
    animal = input()

    letters[animal[0]] += 1
    animals.append(animal)

choices = list(filter(lambda x: x[0] == starting_letter, animals))

print(solve(choices, letters, starting_letter))