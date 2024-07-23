'''Most frequently used words in a text

Write a function that, given a string of text (possibly with punctuation and line-breaks), 
returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, 
or an empty array if a text contains no words.

Examples:

"In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."
--> ["a", "of", "on"]

"e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"
--> ["e", "ddd", "aa"]

"  //wont won't won't"
--> ["won't", "wont"]

Bonus points (not really, but just for fun):
Avoid creating an array whose memory footprint is roughly as big as the input text.
Avoid sorting the entire array of unique words.
'''
# top solution
from collections import Counter
import re


def top_3_words_codewars(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in c.most_common(3)]

# my solution
def top_3_words(text: str):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    text = text.lower()
    text = ''.join(' ' if x not in letters + '\'' else x for x in text)
    words = text.split()

    for word in words:
        if word.find('\'') != -1:
            to_replace = {'word': word[:],
                          'index': words.index(word),
                          'w_len': len(word)}

            for index_letter in range(to_replace['w_len']):
                if word[index_letter] == '\'':
                    #Check for letters near by
                    if to_replace['w_len'] == 1:
                        to_replace['word'] = ''
                    # begin word
                    elif index_letter == 0 and word[1] not in letters:
                        to_replace['word'] = to_replace['word'][1:]
                    # end word    
                    elif index_letter == to_replace['w_len']-1:
                        to_replace['word'] = to_replace['word'][:-2] if word[index_letter - 1] not in letters else to_replace['word']  
                    #middle word    
                    elif word[index_letter - 1] not in letters and word[index_letter + 1] not in letters:
                        to_replace['word'] = to_replace['word'][:index_letter] + to_replace['word'][index_letter + 1:]      

            if to_replace['word'] != '':
                words[to_replace['index']] = to_replace['word'] 
            else:
                words.remove(word)

    count_words = [(words.count(word), word) for word in set(words)]
    return [val for key, val in sorted(count_words,reverse=True)[:3]]    

print(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
print(top_3_words("  //wont won't won't "), ["won't", "wont"])
print(top_3_words("  , e   .. "), ["e"])
print(top_3_words("  ...  "), [])
print(top_3_words("  '  "), [])
print(top_3_words("  '''  "), [])
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])