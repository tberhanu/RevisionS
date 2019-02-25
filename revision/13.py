"""13. Add up all elements of the array
        i)using list compression
        ii) using reduce
"""
from functools import reduce
arr = [1, 2, 3, 4]
summed = sum(arr)
print(summed)

summed2 = reduce(lambda a, b: a+b, arr)
print(summed2)
multiplied = reduce(lambda a, b: a * b, arr)
print(multiplied)
