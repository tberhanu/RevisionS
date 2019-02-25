""" 18. How to add up to floating numbers without discrepancy
    Check if the number is Infinity or Nan
    Create a fraction
    Convert float to fraction

"""
from fractions import Fraction
import math
from decimal import Decimal
d1 = Decimal('2.1')
d2 = Decimal('4.2')
print(d1 + d2)
print(2.1 + 4.2)

a = float("inf")
b = float("-inf")
c = float("nan")
print(math.isinf(a))
print(math.isinf(b))
print(math.isinf(c))
print(math.isnan(c))

f = Fraction(5, 4)
print(f)
f2 = Fraction(7, 16)
print(f + f2)
k = 3.75
k_fraction = Fraction(k)
print(k_fraction)
k_fraction_obj = Fraction(*k.as_integer_ratio())
print(k_fraction_obj)
