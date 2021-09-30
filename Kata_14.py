"""
Day 13 - Greed is Good

Greed is a dice game played with five six-sided dice. Your mission, should you choose to
accept it, is to score a throw according to these rules.
You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point

A single die can only be counted once in each roll. For example, a given "5" can only
count as part of a triplet (contributing to the 500 points) or as a single 50 points,
but not both in the same roll.
"""


# My Solution
from collections import Counter

scoreboard = {
    "1:3": 1000,
    "6:3": 600,
    "5:3": 500,
    "4:3": 400,
    "3:3": 300,
    "2:3": 200,
    "1:1": 100,
    "5:1": 50,
}

def score(dice):
    score_count = 0
    for (k, v) in Counter(dice).items():
        if v%3 == 0:
            score_count += (scoreboard[f"{k}:3"] * v/3)
        else:
            if k in [1,5]:
                mult = int(v/3)
                score_count += (scoreboard[f"{k}:3"] * mult)
                score_count += (scoreboard[f"{k}:1"] * v if mult == 0 else mult*3-v)
    return int(score_count)


# Highest rated solution on CodeWars
def score_sol(dice):
    sum = 0
    counter = [0, 0, 0, 0, 0, 0]
    points = [1000, 200, 300, 400, 500, 600]
    extra = [100, 0, 0, 0, 50, 0]
    for die in dice:
        counter[die - 1] += 1

    for (i, count) in enumerate(counter):
        sum += (points[i] if count >= 3 else 0) + extra[i] * (count % 3)

    return sum


if __name__ == '__main__':
    print(score([2, 4, 4, 5, 4]))
