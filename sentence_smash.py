def smash(words):
    '''sentence = ''
    for word in words:
        sentence = sentence + ' ' + word
    
    return sentence.strip()'''
    return ' '.join(words)

words = ['hello', 'world', 'this', 'is', 'great'] 
sentence = smash(words)
print(sentence)