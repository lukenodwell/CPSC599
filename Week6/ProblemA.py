import sys

input_data = sys.stdin.read()
lines = input_data.splitlines()

n = int(lines[0])
weights = [int(lines[i]) for i in range(1, n + 1)]

max_weight = 2000
possible_sums = [0] * (max_weight + 1)
possible_sums[0] = 1

for weight in weights:
    for j in range(max_weight, weight - 1, -1):
        if possible_sums[j - weight]:
            possible_sums[j] = 1

closest_sum = 0
for i in range(max_weight + 1):
    if possible_sums[i]:
        if abs(1000 - i) < abs(1000 - closest_sum) or (abs(1000 - i) == abs(1000 - closest_sum) and i > closest_sum):
            closest_sum = i

print(closest_sum)