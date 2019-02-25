"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

"""


def titleToNumber(s):
    """Runtime: 56 ms, faster than 81.35% of Python3 online submissions for Excel Sheet Column Number.
"""
    ans = 0
    for i in s:
        ans = ans * 26
        ans = ans + ord(i) - 64
    return ans

print(titleToNumber("ZY"))
