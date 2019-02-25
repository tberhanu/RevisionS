"""
Given a string S, we can transform every letter individually to be lowercase or uppercase
to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.

"""

def letter_case_permutation(string):
    """
    Runtime: 68 ms, faster than 77.71% of Python online submissions for Letter Case Permutation.
    """
    arr = []
    i = 0
    return foo(string, arr, i)

def foo(string, arr, i):
    if i == len(string):
        arr.append(string)
    else:
        digits = "0987654321"
        if string[i] not in digits:
            foo(string, arr, i + 1)
            s = string[:i] + string[i].swapcase() + string[i+1:]
            foo(s, arr, i + 1)
        else:
            foo(string, arr, i + 1)
    return arr
print(letter_case_permutation("a1b2"))