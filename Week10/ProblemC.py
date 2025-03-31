import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()
    
r, c = map(int, data[0].split())
mat = [list(data[i + 1]) for i in range(r)]
    
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [1, 1, 1, 0, -1, -1, -1, 0]
    
def dfs(rr, cc):
        mat[rr][cc] = '.'
        for i in range(8):
                new_r, new_c = rr + dx[i], cc + dy[i]
                if valid(new_r, new_c) and mat[new_r][new_c] == '#':
                        dfs(new_r, new_c)
    
def valid(rr, cc):
        return 0 <= rr < r and 0 <= cc < c
    
total = 0
for i in range(r):
        for j in range(c):
                if mat[i][j] == '#':
                        total += 1
                        dfs(i, j)
    
print(total)
