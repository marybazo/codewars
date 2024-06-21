def sum_array(arr):
    '''if type(arr) != type(list()):
        return 0
   
    arr.sort()   
    summa = 0    
    for i in range(1,len(arr)-1, 1):
        summa += arr[i]

    return summa'''
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)  


arr = [6, 2, 1, 8, 10]
arr = None
summa = sum_array(arr)
print(summa)  
