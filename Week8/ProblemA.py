from itertools import permutations

class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    def __lt__(self, other):
        if self.y == other.y:
            if self.m == other.m:
                return self.d < other.d
            return self.m < other.m
        return self.y < other.y

    def __eq__(self, other):
        return self.d == other.d and self.m == other.m and self.y == other.y

    def __hash__(self):
        return hash((self.d, self.m, self.y))

def leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def works(date):
    if date.d < 1 or date.m < 1 or date.y < 2000:
        return False
    if date.m > 12:
        return False

    days = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap(date.y):
        days[2] += 1

    if date.d > days[date.m]:
        return False

    return True

def solve():
    v = input().split()
    b = []

    for date in v:
        date.split()
        for i in range(len(date)):
            j = int(date[i])
            b.append(j)

    perm = list(permutations(b))
    good = set()

    for p in perm:
        d = p[0] * 10 + p[1]
        m = p[2] * 10 + p[3]
        y = p[4] * 1000 + p[5] * 100 + p[6] * 10 + p[7]
        date = Date(d, m, y)
        if works(date):
            if date not in good:
                good.add(date)

    print(len(good), end=" ")
    if len(good) > 0:
        d = min(good)
        print(f"{d.d:02d} {d.m:02d} {d.y}")
    else:
        print()

n = int(input())
for _ in range(n):
        solve()