"""
Day 2

In this little assignment you are given a string of space separated numbers,
and have to return the highest and lowest number.
"""


# My Solution
def high_and_low(numbers):
    list = [int(x) for x in numbers.split()]
    list.sort()
    return f"{list[-1]} {list[0]}"


# Highest rated solution on CodeWars
def high_and_low_sol(numbers):
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
