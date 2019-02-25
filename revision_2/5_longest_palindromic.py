"""
1. Given a str, what is the longest palindrome
"""

def longest_palindrome(string):
    """
    Runtime: 5116 ms, faster than 19.32% of Python3 online submissions for Longest Palindromic Substring.

    """
    if string == "":
        return ""
    i = 0
    pal = string[0]
    while i < len(string):
        j = len(string)
        if len(string[i:j]) <= len(pal):
                return pal
        while j >= 0:
            if string[i:j] == string[i:j][::-1]:
                if len(string[i:j]) > len(pal):
                    pal = string[i:j]
                break
            j = j - 1
        i = i + 1
    return pal

def get_length(string):
    if string == string[::-1]:
        return len(string)
    else:
        return max(get_length(string[1:]), get_length(string[:-1]))


print(longest_palindrome('eabcb'), get_length('eabcb'))
print(longest_palindrome("babad"), get_length('babad'))
print(longest_palindrome("b"), get_length('b'))
print(longest_palindrome("baabaabk"), get_length("baabaabk"))
print(longest_palindrome("baab"), get_length("baab"))
print(longest_palindrome("abcdefg"), get_length("abdefg"))
print(longest_palindrome("bananas"), get_length("bananas"))
