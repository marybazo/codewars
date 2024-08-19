'''
Given an array of positive or negative integers
I= [i1,..,in]

you have to produce a sorted array P of the form
[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given
as a string in Java, C#, C, C++ and as an array of arrays in other languages.

Example:
I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes:
It can happen that a sum is 0 if some numbers are negative!
'''

import math
def sum_for_list(lst):

    p_factor = []
    num_prime = []
    for num in lst:
        prime = primeFactors(num)
        p_factor.extend(prime)
        num_prime.append([num, prime])

    result = []
    for i in sorted(list(set(p_factor))):
        sum = 0
        for pair in num_prime:
            if i in pair[1]:
                sum += pair[0]
        result.append([int(i), sum])

    return result


# A function to print all prime factors of a given number n
def primeFactors(n):

    prime_factors = []
    n = abs(n)
    
    # Print the number of two's that divide n
    while n % 2 == 0:
        prime_factors.append(2)
        n = n / 2
        
    # n must be odd at this point so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n))+1, 2):
        
        # while i divides n, print i ad divide n
        while n % i == 0:
            prime_factors.append(i)
            n = n / i
            
    # Condition if n is a prime number greater than 2
    if n > 2:
        prime_factors.append(n)
    
    return prime_factors       

# best solution from codewars.com
from collections import defaultdict
def sum_for_list_best(lst):

    def factors(x):
        p_facs = []
        i = 2
        while x > 1 or x < -1:
            if x % i == 0:
                p_facs.append(i)
                x //= i
            else:
                i += 1
        return list(set(p_facs))
    
    fac_dict = defaultdict(int)
    
    for i in lst:
        for fac in factors(i):
            fac_dict[fac] += i
            
    return sorted([[k,v] for k,v in fac_dict.items()])

# a = [12, 15]
# print(sum_for_list(a) == [[2, 12], [3, 27], [5, 15]])

a = [-29804, -4209, -28265, -72769, -31744]
b = [ [2, -61548], [3, -4209], [5, -28265], [23, -4209], [31, -31744], [53, -72769], [61, -4209], [1373, -72769], [5653, -28265], [7451, -29804] ]
print(sum_for_list(a))
print(b)