""" 25. Make a dict using array1 as key and array2 as value
        Zipping more than two elements of the tuple
        Traverse thru arr1, and continue traversing to arr2 without concatenating them-->CHAIN
"""
from itertools import chain
arr1 = ["fname", "lname", "year"]
arr2 = ["John", "Bora", "Senior"]
dictionary = dict(zip(arr1, arr2))
print(dictionary)

for k, v in zip(arr1, arr2):
    print(k,v)
print("****")
for x in chain(arr1, arr2):
    print(x)
print("--------------------")
arr3 = [1, 2, 3]
for a, b, c in zip(arr1, arr2, arr3):
    print(a, b, c)
