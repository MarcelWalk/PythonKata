"""
Day 6 - Array.diff

Your goal in this kata is to implement a difference function, which subtracts one list
from another and returns the result.
It should remove all values from list a, which are present in list b keeping their order.
"""


# My Solution
def array_diff(src_arr, comp_arr):
    output = []

    [output.append(src_arr[x]) if src_arr[x] not in comp_arr else None for x in range(len(src_arr))]

    return output


# Highest rated solution on CodeWars
def array_diff_sol(a, b):
    return [x for x in a if x not in b]
