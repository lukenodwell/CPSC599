import sys

input_data = sys.stdin.read()

lines = input_data.splitlines()

t = int(lines[0])

for i in range(1, t + 1):
    kids, candies = lines[i].split()

    kids = int(kids)

    candies = int(candies)

    if (kids == 1):
        print(2)
        continue

    if (candies == 1):
        print(kids + 1)
        continue

    a, b = candies, kids

    x0, x1 = 1, 0

    while b:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1

    if a != 1:
        print("IMPOSSIBLE")
        continue

    print(x0 % kids)