import sys
import math

input_data = sys.stdin.read()

line = input_data

m, n, t = line.split()
m = int(m)
n = int(n)
t = int(t)

computes = 0

if t == 1:
        # O(n!)
        computes = 1
        for i in range(1, n + 1):
                computes *= i
                if computes > m:
                        break
elif t == 2:
        # O(2^n)
        computes = 2**n
elif t == 3:
        # O(n^4)
        computes = n**4
elif t == 4:
        # O(n^3)
        computes = n**3
elif t == 5:
        # O(n^2)
        computes = n**2
elif t == 6:
        # O(n log n)
        computes = n * math.log2(n)
elif t == 7:
        # O(n)
        computes = n
# print("Computes: ", computes)
# print("m: ", m)
if m >= computes:
        print("AC")
else:
        print("TLE")