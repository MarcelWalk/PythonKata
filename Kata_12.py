"""
Day 11 - Moving Zeros To The End

Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
"""


# My Solution
def move_zeros(array):
    zero_count = 0
    arr = []

    for element in array:
        if element == 0:
            zero_count += 1
        else:
            arr.append(element)

    arr.extend([0 for i in range(zero_count)])
    return arr


# Highest rated solution on CodeWars
def move_zeros_sol(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
