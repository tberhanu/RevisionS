""" 21. Create iterator from an array,
        and Slice the iterator
"""
arr = [1, 2, 3]
it = iter(arr)
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

def count(n):
    while True:
        yield n
        n = n + 1

c = count(0)
import itertools
arr = [x for x in itertools.islice(c, 10, 20)]
print(arr)
