import sys

input_data = sys.stdin.read()
lines = input_data.splitlines()

n = int(lines[0])
cars = [int(lines[i]) for i in range(1, n + 1)]

def longest_increasing_subsequence(arr):
    lis = [1] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        for j in range(len(arr) - 1, i, -1):
            if arr[i] < arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return lis

def longest_decreasing_subsequence(arr):
    lds = [1] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        for j in range(len(arr) - 1, i, -1):
            if arr[i] > arr[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1
    return lds

lis = longest_increasing_subsequence(cars)
lds = longest_decreasing_subsequence(cars)

max_length = 0
for i in range(n):
    max_length = max(max_length, lis[i] + lds[i] - 1)

print(max_length)