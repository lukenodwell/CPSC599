import sys

input_data = sys.stdin.read()

lines = input_data.splitlines()

# Number of cases
n = int(lines[0])

startingIndex = 2

for j in range (1, n + 1):
        # Get the number of kids per case
        kids = int(lines[startingIndex])

        startingIndex += 1

        totalCandies = 0

        for i in range(startingIndex, kids + startingIndex):
                totalCandies += int(lines[i])

        if totalCandies % kids == 0:
                print("YES")
        else:
                print("NO")

        startingIndex += kids + 1 # Offset for next case