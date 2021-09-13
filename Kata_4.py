"""
In this kata you will create a function that takes a list of non-negative integers and
strings and returns a new list with the strings filtered out.
"""


# My Solution
def filter_list(l):
  r = []
  [r.append(x) if type(x) == int else None for x in l]
  return r



# Highest rated solution on CodeWars
def filter_list_sol(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]
