""" 2. Get n largest/smallest element of the array
"""
import heapq
arr = [4, 3, 6, 7, 1, 2, 5]
print(heapq.nlargest(4, arr))
print(heapq.nsmallest(3, arr))
