import sys

input_data = sys.stdin.read()

lines = input_data.splitlines()

for line in lines:
    a, b = line.split()
    a = int(a)
    b = int(b)
    print(abs(a - b))