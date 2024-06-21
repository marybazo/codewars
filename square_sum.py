def square_sum(numbers):
    sum = 0
    for n in numbers:
        sum += n**2
    return sum    
    #return sum(x ** 2 for x in numbers)