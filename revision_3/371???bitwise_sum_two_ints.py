"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
"""

def get_sum(a, b):
    while b != 0:
        carry = a & b

        a = a^b
        b = carry << 1
    return a

print(get_sum(3, 4))
print(get_sum(-9, 7))