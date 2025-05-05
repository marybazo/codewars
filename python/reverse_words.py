def reverse_words(text:str):
    '''text_list = text.split(' ')
    res = str()
    for word in text_list:
        res += word[::-1] + ' '    
    return res.strip()'''
    t = ' '.join(s[::-1] for s in text.split(' '))  
    return t   

print(reverse_words('The quick brown fox jumps over the lazy dog.'))