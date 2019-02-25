# arr = [1, 1, 2, 3, 4, 2, 5, 5, 4, 2]
# arr2 = []
# sets = set()
# for a in arr:
#     if a not in sets:
#         arr2.append(a)
#         sets.add(a)
# print(arr2)


# arr = [1, 1, 2, 3, 4, 2, 5, 5, 4, 2]
# dict = {}
# uniques = [dict.setdefault(a, a) for a in arr if a not in dict]
# print(uniques)

arr = [{"name": 1, "age": 88}, {"name": -4, "age": 9}, {"name": 3, "age": 6}, {"name": 4, "age": -8}]
# arr.sort()
print(arr)
a = sorted(arr, key=lambda kv: kv["age"])
b = sorted(arr, key=lambda kv: kv["name"])

print(a)
print(b)
