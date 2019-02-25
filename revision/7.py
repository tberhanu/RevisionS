""" 7. Create dictionary whose default value is 99
"""
from collections import defaultdict
dict = {1: 2, 2: 3, 3: 4}
d = defaultdict(lambda: 99, dict)
print(d)
print(d[1])
print(d[5])
