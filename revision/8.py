""" 8. Create dictionary that keeps elements in order of the key
"""
from collections import OrderedDict
dict = {1: "hello", 2: "Hey", 5: "kef", 3: "shake"}
d = OrderedDict(dict)
print(d)
d[4] = "new"
print(d)
print(dict)
