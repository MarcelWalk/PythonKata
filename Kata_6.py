"""
Day 5

Create a function taking a positive integer as its parameter and returning a string
containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the
left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is
rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII;
or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
"""


# My Solution
roman_nums = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
}


def solution(n: str):
    n_str = str(n)
    return "".join(get_numeral(n_str[x], (10 ^ x)) for x in range(len(n_str)))


def get_numeral(no, multi: int):
    no = int(no)

    if no >= 5:
        base = 5 * multi
        if no == 5:
            return roman_nums[base]
        else:
            fill_char = roman_nums[base / 5]
            return roman_nums[base].rjust((no * multi) - base, fill_char)


    else:
        base = 1 * multi
        if no == 1:
            return roman_nums[base]
        else:
            fill_char = roman_nums[base]
            return "".rjust(no, fill_char)
