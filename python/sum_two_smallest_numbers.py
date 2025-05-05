def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return sum(numbers[:2])    


    



numbers = [19, 5, 42, 2, 77]
summa = sum_two_smallest_numbers(numbers)
print(summa)
