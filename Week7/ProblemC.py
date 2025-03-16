def print_state(x):
    if x == 0:
        return "NNN"
    if x == 1:
        return "NNY"
    if x == 2:
        return "NYN"
    if x == 3:
        return "NYY"
    if x == 4:
        return "YNN"
    if x == 5:
        return "YNY"
    if x == 6:
        return "YYN"
    if x == 7:
        return "YYY"

rel = [
    [1, 2, 4],
    [0, 3, 5],
    [0, 3, 6],
    [1, 2, 7],
    [0, 5, 6],
    [1, 4, 7],
    [2, 4, 7],
    [3, 5, 6]
]

import sys
input = sys.stdin.read
data = input().split()

index = 0
n = int(data[index])
index += 1
results = []

for _ in range(n):
    m = int(data[index])
    index += 1
    a = []
    for _ in range(m):
        a.append(list(map(int, data[index:index+8])))
        index += 8

    f = [[0] * 8 for _ in range(m)]

    for i in range(8):
        t0 = a[m-1][rel[i][0]]
        t1 = a[m-1][rel[i][1]]
        t2 = a[m-1][rel[i][2]]
        if t0 < t1 and t0 < t2:
            f[m-1][i] = rel[i][0]
        elif t1 < t2:
            f[m-1][i] = rel[i][1]
        else:
            f[m-1][i] = rel[i][2]

    for k in range(m-2, -1, -1):
        for i in range(8):
            t0 = a[k][f[k+1][rel[i][0]]]
            t1 = a[k][f[k+1][rel[i][1]]]
            t2 = a[k][f[k+1][rel[i][2]]]
            if t0 < t1 and t0 < t2:
                f[k][i] = f[k+1][rel[i][0]]
            elif t1 < t2:
                f[k][i] = f[k+1][rel[i][1]]
            else:
                f[k][i] = f[k+1][rel[i][2]]

    results.append(print_state(f[0][0]))

for result in results:
    print(result)