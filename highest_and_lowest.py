def high_and_low(numbers):
    '''l_srt_numbers = numbers.split(' ')
    l_int_numbers = [int(x) for x in l_srt_numbers]'''
    l_int_numbers = [int(x) for x in numbers.split(' ')]

    '''l_int_numbers.sort()
    return str(l_int_numbers[len(l_int_numbers)-1]) + ' '+ str(l_int_numbers[0])'''
    return str(max(l_int_numbers)) + ' ' + str(min(l_int_numbers))
    #return "%i %i" % (max(nn),min(nn))
     

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")) 