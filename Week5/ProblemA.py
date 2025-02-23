import sys

def lowest_order_non_zero_digit(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    
    
    while factorial % 10 == 0:
        factorial //= 10

    return factorial % 10

input_data = sys.stdin.read()
lines = input_data.splitlines()

for line in lines:
    line = int(line)
    if line != 0:
        last_non_zero_digit = lowest_order_non_zero_digit(line)
        print(last_non_zero_digit)