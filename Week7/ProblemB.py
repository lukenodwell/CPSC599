def min_switches(n, m, instruments, tune):
    dp = [[float('inf')] * n for _ in range(m)]
    
    for i in range(n):
        if tune[0] in instruments[i]:
            dp[0][i] = 0
    
    for j in range(1, m):
        for i in range(n):
            if tune[j] in instruments[i]:
                for k in range(n):
                    if dp[j-1][k] != float('inf'):
                        if i == k:
                            dp[j][i] = min(dp[j][i], dp[j-1][k])
                        else:
                            dp[j][i] = min(dp[j][i], dp[j-1][k] + 1)
    
    result = min(dp[m-1])
    return result


import sys
input = sys.stdin.read
data = input().split()
    
n = int(data[0])
m = int(data[1])
    
instruments = []
index = 2
for _ in range(n):
        k = int(data[index])
        notes = list(map(int, data[index+1:index+1+k]))
        instruments.append(notes)
        index += k + 1
    
tune = list(map(int, data[index:index+m]))
    
print(min_switches(n, m, instruments, tune))