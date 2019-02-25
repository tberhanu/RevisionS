""" 12. Filter only the evens of the array
        i) using list compresssion
        ii) using filter
"""
arr = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [e for e in arr if e%2==0]
print(evens)

odds = list(filter(lambda e: e%2 != 0, arr))
print(odds)
