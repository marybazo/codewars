"""
Your task is to make a function that can take any non-negative integer as an argument 
and return it with its digits in descending order. Essentially, rearrange the digits 
to create the highest possible number.

Examples:
Input: 42145 Output: 54421
"""

def descending_order(num):
    if num < 0:
        raise Exception('Negative input!')
    
    l_num = sorted([int(n) for n in str(num)], reverse=True)
    str_a = ''
    for n in l_num:
        str_a += str(n) 
    return int(str_a)

    # Same logic in 1 line
    # return int("".join(sorted(str(num), reverse=True)))
        
descending_order(0)