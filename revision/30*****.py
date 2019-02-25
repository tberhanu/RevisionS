""" How to make a counter class that also remembers the order in which it first found something.

Get the most repeated char of the given string. If two chars occur same number of times,
return in alphabetical order.
"""
from collections import Counter, OrderedDict

class CounterOrderedDict(Counter, OrderedDict):
    pass


def foo(string):
    esp_cntr = CounterOrderedDict(sorted(string))

    return esp_cntr.most_common(1)

s = "zzzbbbcccaaa"
print(foo(s))
