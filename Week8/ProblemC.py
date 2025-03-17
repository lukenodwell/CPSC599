import sys

lines = sys.stdin.readlines()
p = int(lines.pop(0))

def checkIsland(list, i):
    sum = 0
    for j in range(1, len(list) - i):
        if max(list[j - 1], list[j + i]) < min(list[j : j + i]):
            sum += 1
    return sum

def islands(lis):
        count = 0
        for i in range(1, 11):
                count += checkIsland(lis, i)
        return count
        
for i in range(1, p + 1):
        islandCount = islands(list(map(int,lines[i-1].split())))
        print(f'{i} {islandCount}')