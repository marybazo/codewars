def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    
    count_numbers = 0
    sum_minus_numbers = 0
    for n in arr:
        if n == 0:
             None
        elif n > 0:    
            count_numbers += 1
        else:
            sum_minus_numbers += n    
    return [count_numbers, sum_minus_numbers]

l = []
print(count_positives_sum_negatives(l))