""" 24. Traverse thru array by enumerating starting from 1
"""
arr = [1, 2, 3]
for i, a in enumerate(arr):
    print(i, a)
for i, a in enumerate(arr, 1):
    print(i, a)
