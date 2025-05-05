def solution(string): 
    '''text = ''   
    for i in reversed(range(0,len(string))):
        text = text + string[i]
    return text   '''

    return string[::-1] 

text = solution('qwerty')
print(text)