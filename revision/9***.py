""" 9. Get min/max of the dict based on the key/value
    Get min/max of the tuples
    Zip is an iterator, change it to list
"""
dict = {1: "hello", 2: "Ha", 5: "kef", 3: "shake"}
# d = max(dict, key=lambda kv: kv[0])
print(max(dict))
print(min(dict))
print(max((1,2,888),(99,7,8),(3,94,8)))
print(max(zip(dict.keys(), dict.values())))
print(min(zip(dict.values(), dict.keys())))

print(list(zip(dict.keys(), dict.values())))
