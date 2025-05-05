"""
Your task is to construct a building which will be a pile of n cubes. 
The cube at the bottom will have a volume of n^3, the cube above will have volume of 
(n - 1)^3 and so on until the top which will have a volume of 1^3.

You are given the total volume m of the building. 
Being given m can you find the number n of cubes you will have to build?

The parameter of the function find_nb will be an integer m and you have to return the integer n 
such as (n - 1)^3 + (n - 2)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

Examples:

find_nb(1071225) --> 45
find_nb(91716553919377) --> -1
"""

# from math import sqrt

# Rule: The sum of the cubes of the first n natural numbers is:
# 1^3 + 2^3 + 3^3 + ... + n^3 = (n(n+1) / 2)^2
# open the ^2 brackets
# n^2 + n - 2*sqrt(m) = 0
# solve quadratic equation and get formula to function

# def find_nb(m):
#     n = (-1 + sqrt(1 + 8 * sqrt(m)))/2
#     if n%1 == 0: 
#         return int(n)
#     else:
#         return -1

def find_nb(m):
    n = 0
    total = 0
    while total < m:
        n += 1
        total += n ** 3
    return n if total == m else -1

print(find_nb(3947374899617627557))