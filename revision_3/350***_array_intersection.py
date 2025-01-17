"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that
you cannot load all elements into the memory at once?
"""

def get_intersect(num1, num2):
    """ Runtime: 44 ms, faster than 60.85% of Python3 online submissions for Intersection of Two Arrays II.
"""
    from collections import Counter
    freq1 = Counter(num1)
    freq2 = Counter(num2)
    arr = []
    for k, v in freq1.items():
        if k in freq2:
            mini = min(v, freq2[k])
            for i in range(mini):
                arr.append(k)
    return arr


print(get_intersect([1,2,2,1], [2]))
print(get_intersect([1,2,2,1], [2, 2]))
print(get_intersect([4,9,5], [9,4,9,8,4]))
