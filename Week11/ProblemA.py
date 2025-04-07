from collections import deque

class Grid:
        def __init__(self, m, n):
                self.m = m
                self.n = n

        def inside_grid(self, row, col):
                return 0 <= row < self.m and 0 <= col < self.n

        def update_d(self, x, y, k, queue, visited, D):
                dis_x = [k, -k, 0, 0]
                dis_y = [0, 0, k, -k]

                for i in range(4):
                        new_x = x + dis_x[i]
                        new_y = y + dis_y[i]
                        if self.inside_grid(new_x, new_y) and not visited[new_x][new_y]:
                                D[new_x][new_y] = D[x][y] + 1
                                visited[new_x][new_y] = True
                                queue.append(new_x * self.n + new_y)

m, n = map(int, input().split())
grid = Grid(m, n)
arr = []
D = [[1_000_000_000] * n for _ in range(m)]

for _ in range(m):
        line = list(map(int, input().strip()))
        arr.append(line)

visited = [[False] * n for _ in range(m)]
queue = deque()
queue.append(0)
D[0][0] = 0
printed = False

while queue:
        u = queue.popleft()
        x = u // n
        y = u % n
        k = arr[x][y]
        if x == m - 1 and y == n - 1:
                print(D[x][y])
                printed = True
                break
        else:
            grid.update_d(x, y, k, queue, visited, D)

if not printed:
        print("-1")