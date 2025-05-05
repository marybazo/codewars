def count_by(x, n):
    """
        Return a sequence of numbers counting by `x` `n` times.
    """
    number_list = list(range(x, x*n + 1, x))
    print(number_list)  

count_by(50,5) 