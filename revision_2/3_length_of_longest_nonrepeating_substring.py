""" https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
def longest_nonrepeating_substring(string):
    """
    Runtime: 740 ms, faster than 11.05% of Python3 online submissions for Longest Substring Without Repeating
    Characters. Memory Usage: 6.9 MB, less than 9.03% of Python3 online submissions for Longest Substring
    Without Repeating Characters.
    """
    if len(string) == 0:
        return 0
    starting_index = [1] * len(string)
    i, j = 0, 1
    while j < len(string):
        if string[j] not in string[i:j]:
            starting_index[i] += 1
            j = j + 1
        else:
            i = i + 1
            j = i + 1

    return max(starting_index)

def lengthOfLongestSubstring(s):
    """Your runtime beats 4.77 % of python submissions.

    """
    if s == " ":
        return 1
    store = set()
    counter = 0
    max_counter = 0
    i = 0
    j = 0
    while i < len(s):
        if s[i] not in store:
            counter = counter + 1
            store.add(s[i])
            if counter > max_counter:
                max_counter = counter
            i = i + 1
        else:
            i = j + 1
            j = j + 1
            counter = 0
            store.clear()
    return max_counter


print(longest_nonrepeating_substring("abcabccebdef"))
print(longest_nonrepeating_substring("dvdf"))
