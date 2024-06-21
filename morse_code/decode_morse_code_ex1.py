'''In this kata you have to write a simple Morse code decoder. 
While the Morse code is now mostly superseded by voice and digital 
data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". 
For example, the letter A is coded as ·−, letter Q is coded as −−·−, 
and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, 
traditionally capital letters are used. 
When the message is written in Morse code, a single space is used to separate 
the character codes and 3 spaces are used to separate words. For example, 
the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

!!!Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes,
the most notorious of those is the international distress signal SOS (that was first issued by Titanic), 
that is coded as ···−−−···. These special codes are treated as single special characters,
and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input 
and return a decoded human-readable string'''

#import for load solution in codewars
#from preloaded import MORSE_CODE

def morse_code_dict():
    return {'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ', ':'--..--', '.':'.-.-.-',
            '?':'..--..', '/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-'}

def morse_decode_letter(character_code: str):
    morse_dict = morse_code_dict()
    #get position from value list and find key in dict
    return list(morse_dict.keys())[list(morse_dict.values()).index(character_code)]

def decode_morse(morse_code: str):
    morse_code = morse_code.strip()
    text = ''
    word_list_code = morse_code.split('   ')
    for word_code in word_list_code:
        letter_list_code = word_code.split(' ')
        for character_code in letter_list_code:
            #for codewars
            #character = MORSE_CODE[character_code]
            character = morse_decode_letter(character_code)
            text += character
        text += ' '    
    return text.strip()

def decode_morse_join_variant(morse_code: str):
    return ' '.join(''.join(morse_decode_letter(letter) for letter in word.split()) for word in morse_code.strip().split('   '))

def decode_morse_recurtion(morse_code: str, text = ''):
    end_word = morse_code.find('   ')
    morse_code = morse_code.strip()
    
    #end recurtion
    if len(morse_code) == 0:
        return text
    
    #last letter in code sentense
    letter_end = morse_code.find(' ')
    if letter_end < 0:
        letter_end = len(morse_code)
    
    #space check
    if end_word == 0:
        text += ' '
    
    if letter_end > 0:    
        text += morse_decode_letter(morse_code[0:letter_end])  
        return decode_morse_recurtion(morse_code[letter_end:], text)   
     


#print(decode_morse_join_variant())
#print(decode_morse('....'))
#print(' '.join(['1','2','3','4']))

print(decode_morse_recurtion('.... . -.--   .--- ..- -.. .'))

    

