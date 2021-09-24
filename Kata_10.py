"""
Day 9 - RGB To Hex Conversion

The rgb function is incomplete. Complete it so that passing in RGB decimal values will
result in a hexadecimal representation being returned. Valid decimal values for RGB are
0 - 255. Any values that fall out of that range must be rounded to the closest
valid value.

Note: Your answer should always be 6 characters long,
the shorthand with 3 will not work here.
"""


# My Solution
def rgb(r, g, b):
    return f"{hex_no(r)}{hex_no(g)}{hex_no(b)}"


def hex_no(num: int):
    if num > 255:
        num = 255
    elif num < 0:
        num = 0
    return f"{hex(num)}".replace("0x","").rjust(2,"0").upper()


# Highest rated solution on CodeWars
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
