import sys

input_data = sys.stdin.read()

lines = input_data.splitlines()

# Number of cases
n = int(lines[0])

for n in range(1, n+1):
        R, B, M = lines[n].split()
        R = float(R)
        B = float(B)
        M = float(M)
        R = R / 100
        possible = True

        payments = 0
        while B > 0:
                if payments == 1200:
                        possible = False
                        print("impossible")
                        break
                payments += 1
                B += B * R
                # print('Loan amount after interest before rounding', B)
                B = round(B, 2)
                # print('Loan amount after interest', B)
                B -= M
        if possible:
                print(payments)