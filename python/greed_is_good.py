"""
Greed is Good
Greed is a dice game played with five six-sided dice. 
Your mission, should you choose to accept it, is to score a throw according 
to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll. 
For example, a given "5" can only count as part of a triplet (contributing to the 500 points) 
or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
Note: your solution must not modify the input list.
"""


def score(dice):
    dice_value = {
        "31": 1000,
        "36": 600,
        "35": 500,
        "34": 400,
        "33": 300,
        "32": 200,
        "1": 100,
        "5": 50,
    }
    summary_score = 0

    for side_score in set(dice):
        side_count = dice.count(side_score)

        if side_count >= 3:
            summary_score += dice_value['3' + str(side_score)]
            side_count -= 3
        
        if side_score == 1 or side_score == 5:
            summary_score += side_count * dice_value[str(side_score)] 
          
        return summary_score


# print(score( [5, 1, 3, 4, 1] ),  250)
# print(score([1, 1, 1, 3, 1]), 1100)
# print(score( [2, 3, 4, 6, 2] ),    0)
# print(score( [4, 4, 4, 3, 3] ),  400)
# print(score( [2, 4, 4, 5, 4] ),  450)
print(score( [2, 2, 2, 2, 3] ),  200)