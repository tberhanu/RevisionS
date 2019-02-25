
"""
Given a 32-bit signed integer, reverse digits of an integer.
"""
def reverse_integer(num):
    """Runtime: 52 ms, faster than 90.09% of Python3 online submissions for Reverse Integer.

    """
    s = int(str(abs(num))[::-1])
    if num < 0:
        s = -1 * s
    if s < -2 ** 31 or s >= 2 ** 31:
        return 0
    return s

print(reverse_integer(-345))