""" 5. Sort the dictionary based on the key/value

"""
dict = {"z": 678, "k": 833, "a": 201, "b": 123, "c": 34, "d": 444}
d = sorted(dict)
print(d)
d = sorted(dict.items())
print(d)
d = sorted(dict.items(), key=lambda kv: kv[0])
print(d )
print(sorted(dict.items(), key=lambda kv: kv[1]))
print(dict)
