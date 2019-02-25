""" 1. Make array where appending and poping is ok on both sides
"""
from collections import deque
arr = [1, 2, 3]
q = deque(arr)


print(q)
q.popleft()
print(q)
q.appendleft("first")
print(q)
q.pop()
print(q)
q.append("last")
print(q)
