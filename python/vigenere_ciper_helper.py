'''
The Vigenère cipher is a classic cipher originally developed by Italian cryptographer Giovan Battista Bellaso 
and published in 1553. It is named after a later French cryptographer Blaise de Vigenère, who had developed 
a stronger autokey cipher (a cipher that incorporates the message of the text into the key).
The cipher is easy to understand and implement, but survived three centuries of attempts to break it, 
earning it the nickname "le chiffre indéchiffrable" or "the indecipherable cipher."

From Wikipedia:
The Vigenère cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers 
based on the letters of a keyword. It is a simple form of polyalphabetic substitution.

In a Caesar cipher, each letter of the alphabet is shifted along some number of places; 
for example, in a Caesar cipher of shift 3, A would become D, B would become E, Y would become B and so on. 
The Vigenère cipher consists of several Caesar ciphers in sequence with different shift values.

Assume the key is repeated for the length of the text, character by character. Note that some implementations 
repeat the key over characters only if they are part of the alphabet -- this is not the case here.

The shift is derived by applying a Caesar shift to a character with the corresponding index of the key in the alphabet.

Visual representation:

"my secret code i want to secure"  // message
"passwordpasswordpasswordpasswor"  // key

var alphabet = 'abcdefghijklmnopqrstuvwxyz';
var key = 'password';

// creates a cipher helper with each letter substituted
// by the corresponding character in the key
var c = new VigenèreCipher(key, alphabet);

c.encode('codewars'); // returns 'rovwsoiv'
c.decode('laxxhsj');  // returns 'waffles'
'''

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz' if alphabet == '' else alphabet
        self.key = 'password' if key == '' else key
        # numerate alphabet
        self.alphabet_max = len(self.alphabet)
        self.alphabet_dict = dict()
        for i, ch in enumerate(self.alphabet):
            self.alphabet_dict[i] = ch
            self.alphabet_dict[ch] = i 

    
    def encode(self, text):
        # map text with key
        text_map = self.key * (len(text) // len(self.key) + 1)
        result_text = ''

        for i, ch in enumerate(text):
            if self.alphabet_dict.get(ch) is None:
                result_text += ch
                continue

            a = self.alphabet_dict[text_map[i]] \
             + self.alphabet_dict[ch] # to what
            if a > self.alphabet_max:
                a = a % self.alphabet_max
            a = 0 if a == self.alphabet_max else a
            result_text += self.alphabet_dict[a]
        
        return result_text
    
    
    def decode(self, text):
        # map text with key
        text_map = self.key * (len(text) // len(self.key) + 1)
        result_text = ''
         
        for i, ch in enumerate(text):
            if self.alphabet_dict.get(ch) is None:
                result_text += ch
                continue
            a = self.alphabet_dict[ch] - self.alphabet_dict[text_map[i]]
            if a < 0:
                a = self.alphabet_max + (a % (-self.alphabet_max)) 
            result_text += self.alphabet_dict[a]
        
        return result_text


c = VigenereCipher('pizza', '')

print(c.encode('asodavwt')) 

c = VigenereCipher('', '')

print(c.encode('codewars'), 'rovwsoiv')
print(c.decode('rovwsoiv'), 'codewars')

print(c.encode('waffles'), 'laxxhsj')
print(c.decode('laxxhsj'), 'waffles')

print(c.encode('CODEWARS'), 'CODEWARS')
print(c.decode('CODEWARS'), 'CODEWARS')
