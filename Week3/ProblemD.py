import sys
from fractions import Fraction

input_data = sys.stdin.read()
lines = input_data.splitlines()

# Number of coefficients
n = int(lines[0])

coefs = list(map(int, lines[1].split()))

def get_fraction(coefs):
    result = Fraction(coefs[-1])
    for coef in reversed(coefs[:-1]):
        result = coef + Fraction(1, result)
    return result

frac = get_fraction(coefs)
print(frac)