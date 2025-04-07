import sys
from math import inf

input = sys.stdin.read
data = input().split()
idx = 0

while True:
    n, m, q = map(int, data[idx:idx+3])
    idx += 3
    if n == 0 and m == 0 and q == 0:
        break

    dist = [[inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u, v, w = map(int, data[idx:idx+3])
        idx += 3
        dist[u][v] = min(dist[u][v], w)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] < inf and dist[k][j] < inf:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    for k in range(n):
        if dist[k][k] < 0:
            for i in range(n):
                for j in range(n):
                    if dist[i][k] < inf and dist[k][j] < inf:
                        dist[i][j] = -inf

    results = []
    for _ in range(q):
        u, v = map(int, data[idx:idx+2])
        idx += 2
        if dist[u][v] == inf:
            results.append("Impossible")
        elif dist[u][v] == -inf:
            results.append("-Infinity")
        else:
            results.append(str(dist[u][v]))
        
    print("\n".join(results))
    print()