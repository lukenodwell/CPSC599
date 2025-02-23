import sys

def lowest_order_non_zero_digits(limit):
    lowest_digits = [1] * (limit + 1)
    factorial = 1

    for i in range(2, limit + 1):
        factorial *= i
        while factorial % 10 == 0:
            factorial //= 10
        factorial %= 10**12
        lowest_digits[i] = factorial % 10

    return lowest_digits

input_data = sys.stdin.read()
lines = input_data.splitlines()
    
limit = 10**6
lowest_digits = lowest_order_non_zero_digits(limit)

for line in lines:
    line = int(line)
    if line == 0:
        break
    print(lowest_digits[line])