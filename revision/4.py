""" 4. i. Get subset of the dict whose value is greater than 200
    ii. Get subset of the dict whose key is greater than 'b'
    iii. Get subset of the dict whose key/value is found in arr
"""
arr = ["a", "c"]
arr2 = [201, 34]
dict = {"a": 201, "b": 123, "c": 34, "d": 444}
sub_dict = {k: v for k, v in dict.items() if v > 200}
print(sub_dict)
sub_dict = {k: v for k, v in dict.items() if k > "b"}
print(sub_dict)
print({k: v for k, v in dict.items() if k in arr})
print({k: v for k, v in dict.items() if v in arr2})
