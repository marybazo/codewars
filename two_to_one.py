#Take 2 strings s1 and s2 including only letters from a to z. 
#Return a new sorted string, the longest possible, 
#containing distinct letters - each taken only once - coming from s1 or s2.
def longest(a1, a2):
    '''l_letters = list()
    for x in a1 + a2:
        if x not in l_letters:
            l_letters.append(x)
    l_letters.sort()
    return ''.join(l_letters) '''
    return ''.join(sorted(set(a1 + a2)))

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a, b)) #abcdefklmopqwxy

a = "abcdefghijklmnopqrstuvwxyz"
print(longest(a, a)) #-> "abcdefghijklmnopqrstuvwxyz"