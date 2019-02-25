""" 3. Get n largest/smallest elts of the array of dicts
"""
import heapq
arr_dicts = [{"name": "John", "age": 23, "city": "Oakland", "state": "CA"},
{"name": "Mary", "age": 33, "city": "San Jose", "state": "CA"},
{"name": "Henock", "age": 27, "city": "Las Vegas", "state": "NV"},
{"name": "James", "age": 19, "city": "Seattle", "state": "WA"}]
# print(arr_dicts)
largests = heapq.nlargest(2, arr_dicts, lambda dict: dict['age'])
print(largests)
smallests = heapq.nsmallest(2, arr_dicts, lambda dict: dict['age'])
print(smallests)
states = heapq.nsmallest(2, arr_dicts, lambda d: d['state'])
print(states)
states = heapq.nlargest(2, arr_dicts, lambda d: d['state'])
print(states)
