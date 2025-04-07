import sys

INF = 10**6

def floyd_warshall(n, edges, queries):
    # Initialize distance matrix
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    # Populate initial distances from edges
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)

    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] < INF and dist[k][j] < INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Detect negative cycles
    for k in range(n):
        if dist[k][k] < 0:
            for i in range(n):
                for j in range(n):
                    if dist[i][k] < INF and dist[k][j] < INF:
                        dist[i][j] = -INF

    # Process queries
    results = []
    for u, v in queries:
        if dist[u][v] == INF:
            results.append("Impossible")
        elif dist[u][v] == -INF:
            results.append("-Infinity")
        else:
            results.append(str(dist[u][v]))
    return results

input = sys.stdin.read
data = input().splitlines()
idx = 0

while idx < len(data):
        n, m, q = map(int, data[idx].split())
        if n == 0:
                break
        idx += 1

        edges = []
        for _ in range(m):
                u, v, w = map(int, data[idx].split())
                edges.append((u, v, w))
                idx += 1

queries = []
for _ in range(q):
        u, v = map(int, data[idx].split())
        queries.append((u, v))
        idx += 1

results = floyd_warshall(n, edges, queries)
sys.stdout.write("\n".join(results) + "\n\n")