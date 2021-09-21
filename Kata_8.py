"""
Day 7 - Format a string of names like 'Bart, Lisa & Maggie'.

Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except
for the last two names, which should be separated by an ampersand.
"""


# My Solution
def namelist(names):
    names = [n["name"] for n in names]
    length = len(names)

    if length == 2:
        return " & ".join(names)
    elif length >= 3:
        return ", ".join(names[:length-1]) + f" & {names[length-1]}"
    else:
        return names[0] if length > 0 else ""


# Highest rated solution on CodeWars
def namelist_sol(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''
