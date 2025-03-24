def setfind(a, v):
    if v[a] < 0:
        return a
    v[a] = setfind(v[a], v)
    return v[a]

def setunion(a, b, v):
    a = setfind(a, v)
    b = setfind(b, v)

    if a == b:
        return

    if v[a] == v[b]:
        v[a] += v[b]
        v[b] = a
        return

    if v[a] > v[b]:
        v[b] += v[a]
        v[a] = b
        return

    if v[a] < v[b]:
        v[a] += v[b]
        v[b] = a
        return

def readint():
    ret = 0
    neg = False
    start = False
    while True:
        r = input()
        if (r < '0' or r > '9') and r != '-' and not start:
            continue
        if (r < '0' or r > '9') and r != '-' and start:
            break
        if start:
            ret *= 10
        start = True
        if r == '-':
            neg = True
        else:
            ret += int(r)
    if neg:
        ret *= -1
    return ret

import sys
input = sys.stdin.read
data = input().split()
idx = 0

n = int(data[idx])
idx += 1
q = int(data[idx])
idx += 1

v = [-1] * (n + 1)

for i in range(q):
        c = data[idx]
        idx += 1
        q1 = int(data[idx])
        idx += 1
        q2 = int(data[idx])
        idx += 1

        if c == '?':
                if setfind(q1, v) == setfind(q2, v):
                        print("yes")
                else:
                        print("no")
        else:
                setunion(q1, q2, v)