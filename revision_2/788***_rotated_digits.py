"""
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number
that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.
A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves;
2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate
to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].
"""
"""                  crazy leetcode both codes accepted but their output differs !!!!           """

def rotated_digits(N):
    """
    :type N: int
    :rtype: int
    """
    best = {"2", "5", "6", "9"}
    # good = ["0", "1", "8"]
    bad = ["3", "4", "7"]
    counter = 0
    i = 1
    while i < N + 1:
        ss = str(i)
        if i > 9 and (ss.startswith(bad[0] or ss.startswith(bad[1]) or str(i).startswith(bad[2]))):
            n = ss.count("0")
            i = i + 10 ** n
            continue
        bad_found = False
        for s in ss:
            if s in bad:
                bad_found = True
                break
        if not bad_found:
            for s in ss:
                if s in best:
                    # print(ss)
                    counter = counter + 1
                    break
        i = i + 1

    return counter
###################################
def rotatedDigits(N):
    """
    :type N: int
    :rtype: int
    """
    s1 = {2, 5, 6, 9}
    # s2 = {0, 1, 2, 5, 6, 8, 9}
    s3 = {3, 4, 7}
    i = 0
    cntr = 0
    while (i <= N):
        num = i
        if has_atleast_one(num, s3):
            i = i + 1
            continue
        if has_atleast_one(num, s1):
            cntr = cntr + 1
        i = i + 1
    return cntr


def has_atleast_one(num, s):
    while (num > 0):
        if num % 10 in s:
            return True
        num = num / 10
    return False



print(rotated_digits(857))
print(rotatedDigits(857))