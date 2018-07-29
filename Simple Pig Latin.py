"""Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldWay !
"""
import re

def pig_it(text):
    words = text.split()
    pig_latin_words = []
    punc_re = re.compile(r'([.,?:;!])')
    for word in words:
        m = punc_re.findall(word)
        print(m)
        word = list(word)

        ending = word.pop(0)+'ay'

        word.append(ending)
        word = ''.join(word)

        pig_latin_words.append(word)




    return ' '.join(pig_latin_words)

print(pig_it('the .quick, brown fox!'))