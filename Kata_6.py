"""
Day 5 - Roman Numerals Encoder

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
    for x in range(len(n_str)):
        print(f"{x} - {pow(10, x)}")
        return "".join(get_numeral(n_str[x], pow(10, x)))


def get_numeral(no, multi: int):
    no = int(no)

    print(f"Got {no} with {multi}")

    # 10 ^ 0 is one so reset multiplier to 0
    # multi = 0 if multi == 1 else multi

    # Stay the same just return
    if no in (5, 1):
        return roman_nums[no * multi]

    # Wired cases IV & IX for example
    elif no in (4, 9):
        next_high = roman_nums[(no + 1) * multi]
        fill = get_numeral(((no + 1) * multi) - no, multi / 10 if multi > 1 else multi)
        return f"{fill}{next_high}"

    # Rest should be straight forward (2,3,6,7,8)
    else:
        base = no * multi
        print(f"Base: {base} ({no} * {multi})")
        if no - 5 < 0:
            fill_char = roman_nums[1 * multi]
            return "".rjust(no, fill_char)
        else:
            fill_char = roman_nums[base - 5]
            print(f"Amount: {base - 4}, fill:{fill_char}")
            return roman_nums[5 * multi].ljust(base - 4, fill_char)
