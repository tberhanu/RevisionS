"""Given an array of integers that is already sorted in ascending order, find two numbers
such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the
target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same
element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

"""


def twoSums(numbers, target):
    """ TOO SLOW, need to use advantage of being sorted
    Your runtime beats 3.01 % of python3 submissions.
    """
    for i in range(len(numbers)):
        diff = target - numbers[i]
        if diff in numbers[i+1:]:
            return [i+1, 1 + numbers[i+1:].index(diff) + len(numbers[:i+1])]

def twoSum(numbers, target):
    """ Let's use advantage of it's being SORTED
    Runtime: 36 ms, faster than 99.51% of Python3 online submissions for Two Sum II - Input array is sorted.

     """
    i, j = 0, len(numbers) - 1
    while i < j:
        sum = numbers[i] + numbers[j]
        if sum == target:
            return [i+1, j+1]
        if sum > target:
            j = j - 1
        if sum < target:
            i = i + 1

print(twoSum([0,0,3,4], 0))
print(twoSum([2,7,11,15], 9))
print(twoSum([2,7,11,15], 18))
print(twoSum([2,7,11,15], 26))

