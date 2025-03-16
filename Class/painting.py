import sys

inputs = sys.stdin.read().splitlines()
n = int(inputs[0])
colours = inputs[1].split()

m = int(inputs[2])
conflicts = []
for i in range(m):
        pair = inputs[3 + i].split()
        conflicts.append((pair[0], pair[1]))

# Recursively computes the number of valid colourings
def colour(used, last, found):

        if (used == (1<<n)-1):
                if not found:
                        print('Found!')
                        return(1, [last])
                return (1, [])
        
        total = 0
        coloursused = []
        
        for i in range(n):
                if (used & (1<<i)):
                        continue
                if ((colours[i], last) in conflicts) or ((last, colours[i]) in conflicts):
                        continue

                result = colour(used | (1<<i), colours[i], found)
                total += result[0]
                if not result[1]:
                        coloursused = [last] + result[1]

        return (total, coloursused)

result = colour(0, None, False)
print(f"Optimal: {result[1]}")
print(f"Count: {result[0]}")