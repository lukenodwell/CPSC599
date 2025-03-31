def find(d, a):
    if d[a] == -1:
        return a
    d[a] = find(d, d[a])
    return d[a]

def join(d, a, b):
    a = find(d, a)
    b = find(d, b)
    if a == b:
        return
    d[a] = b

n, m, k = map(int, input().split())

d1 = [-1] * n
d2 = [-1] * n

for _ in range(m):
        c, n1, n2 = input().split()
        n1, n2 = int(n1) - 1, int(n2) - 1

        if c == 'R':
                join(d1, n1, n2)
        else:
                join(d2, n1, n2)

blue_avail = sum(1 for i in range(n) if d2[i] != -1)

blue_need = sum(1 for i in range(n) if d1[i] == -1) - 1

if blue_avail < k or blue_avail < blue_need or blue_need > k:
        print(0)
else:
        print(1)
