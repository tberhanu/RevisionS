""" 11. Count how many times each element found inside a string/array
    Why do you use +/- between two counters--> to get the counting number difference
    which id completely different from that of dictionaries +/-
    ** Convert the Counter to Dictioinary

"""

from collections import Counter
string = "Hello world let's count them He Hello them"
print(string.count("H"))
print(string.count("He"))
print(string.count("Hello"))
counter = Counter(string)
print(counter)
print(counter.keys())
print(counter.values())
print("counter max key: {}".format(max(zip(counter.keys(), counter.values()))))
arr = [1, 1, 2, 3, 3, 3, 4, 1, 1]
counter2 = Counter(arr)
print(counter2)
print(max(counter2))
print(min(counter2))
print("counter max key: {}".format(max(zip(counter2.values(), counter2.keys()))))
arr2 = [1, 2, 2, 3]
counter3 = Counter(arr2)
print("counter2: {}".format(counter2))
print("counter3: {}".format(counter3))
print("counter2 - counter3: {}".format(counter2 - counter3))

dict3 = dict(counter3)
print(dict3)
