""" 10. Get common keys found in both the dict1 and dict2
    Get keys found in dict1 but not in dict2
    Get common k, v pairs found in both dict1 and dict2
    Get the common characters/strings b/n str1 and str2
"""

dict1 = {10: 2, 30: 4, 50: 6, 31: 31, 21: 21}
dict2 = {11: 11, 21: 21, 31: 31, 51: 51, 10: 200}

intersection = dict1.items() & dict2.items()
print("intersection of dict.items() : {}".format(intersection))
print("intersection of dict.values() : {}".format(dict1.keys() & dict2.keys()))
difference = dict1.items() - dict2.items()
print("difference of items(): {}".format(difference))
print("difference of items(): {}".format(dict2.items() - dict1.items()))

str1 = "hello"
str2 = "warling"
print(set(str1) & set(str2))
str1 = "heee"
str2 = "warengerh"
print(set(str1) & set(str2))
