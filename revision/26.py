""" 26. Merge two already sorted arrays while the merged array remain sorted-->heapq
    ** Given nested array flatten it--> yield from
    *** How to know if a thing is an Iterable
"""
import heapq
a = [1, 4, 7]
b = [2, 5, 6, 9]
arr = [e for e in heapq.merge(a, b)]
print(arr)
print(type(9) == int)
print(type(4.09) == float)
print(type(True) == bool)
from collections import Iterable
print(isinstance(a, Iterable))
print(isinstance(arr, Iterable))
print("Look : {}".format(type("string") is str))
print("Look : {}".format(type("string") == str))

def flatten(arr):
    for a in arr:
        if isinstance(a, Iterable):
            yield from flatten(a)
        else:
            yield a

arr = [1, 2, [3, 4, [5, 6, [7]]], 8, [9, 10]]
print(list(flatten(arr)))
