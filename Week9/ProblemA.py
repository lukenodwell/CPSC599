import sys

input = sys.stdin.read
data = input().splitlines()

index = 0
while index < len(data):
    s = data[index]
    index += 1
    if s == '-1':
        break

    n = int(s)
    v = []
    for i in range(n):
        v.append(list(map(int, data[index].split())))
        index += 1

    weak_vertices = []
    for i in range(n):
        weak = True
        for j in range(n):
            for k in range(n):
                if v[i][k] == 1 and v[i][j] == 1 and v[j][k] == 1 and i != k and i != j and j != k:
                    weak = False
        if weak:
            weak_vertices.append(i)

    print(" ".join(map(str, weak_vertices)))