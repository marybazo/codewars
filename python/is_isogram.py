def is_isogram(word:str):
    return len(list(word)) == len(set(word))

'''isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false'''

print(is_isogram('Dermatoglyphics'))
print(is_isogram('moose'))
print(is_isogram('aba'))