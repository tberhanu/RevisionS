""" 23. Use permutations and combinations
"""

from itertools import permutations, combinations
arr = [1, 2, 3, 4]
arr2 = [e for e in permutations(arr)]
print(arr2)
arr3 = [e for e in combinations(arr, 3)]
print(arr3)

# print(permutations(arr))
# print(combinations(arr, 4))
