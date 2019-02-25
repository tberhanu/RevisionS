""" 22. Exclude the first characters of some kind, and collect the rest--> DROPWHILE
"""
from itertools import dropwhile
string = "#####***@@ HELLO world"
lst = [e for e in dropwhile(lambda a: a == "#", string)]
print(lst)
arr = ["#", "*"]
lst = [e for e in dropwhile(lambda a: a in arr, string)]
print(lst)

str = "#*@"
lst = [e for e in dropwhile(lambda a: a in str, string)]
print(lst)
