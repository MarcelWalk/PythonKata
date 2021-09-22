"""
Day 8 - Maximum subarray sum

The maximum sum subarray problem consists in finding the maximum sum of a contiguous
subsequence in an array or list of integers:
Easy case is when the list is made up of only positive numbers and the maximum sum is the
sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is
also a valid sublist/subarray.
"""


# My Solution
def max_sequence(arr):
    highest_sum = 0

    if len(arr) == 0:
        return 0

    for x in range(len(arr)+1):
        for y in range(len(arr)+1):
            if (sum(arr[x:y])) > highest_sum and x != y:
                highest_sum = sum(arr[x:y])

    return highest_sum


# Highest rated solution on CodeWars
def max_sequence_sol(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max
