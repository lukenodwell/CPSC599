import sys
from decimal import Decimal, ROUND_HALF_UP

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

    payments = 0
    while B > 0:
        if payments == 1200:
            possible = False
            print("impossible")
            break
        payments += 1
        OG_B = B
        B += B * R
        # print('Loan amount after interest before rounding', B)
        # Allow for rounding to the nearest 0.5 cents
        B = B.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
        # print('Loan amount 3 digits', B)
        # Then round to the nearest cent
        B = B.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        if OG_B - B > M:
            print("impossible")
            break
        # print('Loan amount after interest', B)
        B -= M
    if possible:
        print(payments)