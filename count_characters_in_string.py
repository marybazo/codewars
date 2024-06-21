"""
The main idea is to count all the occurring characters in a string. 
If you have a string like 'aba', then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""

def count(s):
    # The function code should be here
    character_count = dict()
    while len(s) != 0:
        character_count[s[0]] = s.count(s[0])
        s = str.replace(s, s[0], '')
    
    return character_count

s = 'aba'
print(count(s)) 
print(s)