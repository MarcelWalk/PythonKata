"""
Day 10 - Count characters in your string

The main idea is to count all the occurring characters in a string.
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""


# My Solution
import collections
def count(string):
    return collections.Counter(string)


# Highest rated solution on CodeWars
from collections import Counter
def count(string):
    return Counter(string)
