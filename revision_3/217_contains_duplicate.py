"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

def contains_duplicate(nums):

    from collections import Counter
    freq = Counter(nums)
    return any(True if v > 1 else False for k, v in freq.items())

def contains_duplicate_better(nums):
    return len(list(set(nums))) != len(nums)

print(contains_duplicate_better([1, 2, 3, 11]))