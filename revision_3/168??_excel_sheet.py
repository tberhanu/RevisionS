"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""
def convertToTitle(n):
    """Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Excel Sheet Column Title.
"""
    arr = []
    while n > 0:
        n = n - 1
        letter = (n % 26) + 65
        letter = chr(letter)
        arr.insert(0, letter)
        n = n // 26
    return "".join(arr)

print(convertToTitle(701))