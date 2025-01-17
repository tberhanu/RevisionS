"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A,
followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000

"""

def sort_array_by_parity(A):
    """
    Time Complexity: O(n)
    Space Complexity: O(1) since we're doing IN PLACE 
    """

    i = 0
    loop = 0
    while loop < len(A):
        if A[i] % 2 == 0:
            i = i + 1
            continue
        else:
            A.append(A[i])
            del A[i]
        loop = loop + 1




A = [3, 1, 2, 4]
sort_array_by_parity(A)
print(A)