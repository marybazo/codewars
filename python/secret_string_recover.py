'''
There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. 
"whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they are valid triplets and that they 
contain sufficient information to deduce the original string. 
In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.
'''

def recover_secret(triplets):
    phrase_letters = list()
    for triplet in triplets:
        in_a, in_b, in_c = None, None, None
        a, b, c = triplet

        if a not in phrase_letters: 
            phrase_letters.insert(0, a)
        in_a = phrase_letters.index(a)

        if b not in phrase_letters: 
            phrase_letters.insert(in_a + 1, b)
        in_b = phrase_letters.index(b)

        if in_a > in_b:
            phrase_letters.insert(in_a + 1, b)
            del(phrase_letters[in_b])
            in_b = in_a + 1

        if c not in phrase_letters: 
            phrase_letters.insert(in_b + 1, c)
        in_c = phrase_letters.index(c)

        if in_b > in_c: 
                phrase_letters.insert(in_b + 1, c)
                del(phrase_letters[in_c])    

    return ''.join(a for a in phrase_letters)

secret = "whatisup"
triplets = [
          ['t','u','p'],
          ['t','u','t'],
          ['w','h','i'],
          ['t','s','u'],
          ['a','t','s'],
          ['h','a','p'],
          ['t','i','s'],
          ['w','h','s']
        ]

print(recover_secret(triplets))

triplets = [
            ['t', 'u', 'p'], 
            ['w', 'h', 'i'], 
            ['t', 's', 'u'], 
            ['a', 't', 's'], 
            ['h', 'a', 'p'], 
            ['t', 'i', 's']
        ]

print(recover_secret(triplets))