import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
k = int(data[2])
r = int(data[3])

len_segments = [0] * (n + 1)
S = [0] * n
C = [0] * n

index = 4
for i in range(1, n + 1):
    len_segments[i] = int(data[index])
    index += 1

for i in range(1, n):
    S[i] = int(data[index])
    C[i] = int(data[index + 1])
    index += 2

inf = 10**17
minDist = [[inf] * (m + 1) for _ in range(n + 1)]
minDist[0][1] = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        maxLaneChanges = len_segments[i] // k
        for l in range(max(1, j - maxLaneChanges), min(m, j + maxLaneChanges) + 1):
            laneChanges = abs(l - j)
            distCurve = 0
            if i > 1:
                distCurve = S[i - 1] + C[i - 1] * l
            minDist[i][j] = min(minDist[i][j], laneChanges * (k + r) + len_segments[i] - laneChanges * k + distCurve + minDist[i - 1][l])

print(minDist[n][1])