"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

An anagram of a string is another string that contains same characters, only the order of
characters can be different. For example, “abcd” and “dabc” are anagram of each other.
"""

def is_anagram(s, t):
    """Runtime: 68 ms, faster than 54.94% of Python3 online submissions for Valid Anagram.
"""
    return sorted(s) == sorted(t)