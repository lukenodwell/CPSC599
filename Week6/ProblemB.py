import sys

input_data = sys.stdin.read()
lines = input_data.splitlines()

n = int(lines[0])
cars = [int(lines[i]) for i in range(1, n + 1)]

dp = [1] * n

for i in range(n):
    for j in range(i):
        if cars[j] < cars[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)

longest_train_length = max(dp) if n > 0 else 0

print(longest_train_length)