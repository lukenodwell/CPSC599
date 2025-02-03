import sys
from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN

input_data = sys.stdin.read()
lines = input_data.splitlines()

# Number of cases
n = int(lines[0])

for i in range(1, n + 1):
    R, B, M = lines[i].split()
    R = Decimal(R) / 100
    B = Decimal(B)
    M = Decimal(M)
    possible = True

    # Early exit if monthly payment is less than the interest accrued in a month
    if M <= B * R:
        print("impossible")
        continue

    payments = 0
    while B > 0:
        if payments == 1200:
            possible = False
            print("impossible")
            break
        payments += 1
        B += B * R
        # Allow for rounding to the nearest 0.5 cents
        B = B.quantize(Decimal('0.001'), rounding=ROUND_DOWN)
        # Then round to the nearest cent
        B = B.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        B -= M
    if possible:
        print(payments)