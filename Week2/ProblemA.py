import sys

input_data = sys.stdin.read()

lines = input_data.splitlines()

time_score = 0
entry_list = []
correct_list = []

hashmap = {}

for line in lines:
        tuple = line.split()
        entry_list.append(tuple)


for entry in entry_list:
        if len(entry) != 3:
                break
        else:
                if entry[2] == 'wrong':
                        hashmap[entry[1]] = hashmap.get(entry[1], 0) + 1
                if entry[2] == 'right':
                        time_score += int(entry[0])
                        correct_list.append(entry[1])

for correct in correct_list:
        time_score += hashmap.get(correct, 0) * 20

print(len(correct_list), time_score)