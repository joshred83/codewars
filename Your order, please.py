"""Your task is to sort a given string. Each word in the String will
contain a single number. This number is the position the word should
have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the
input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s
is2 3a T4est"
"""


def order(sentence):
    words = sentence.split(' ')
    ordered_sentence = [''] * len(words)

    for word in words:
        print()
        for char in word:
            if char.isdigit():
                ordered_sentence.pop(int(char) - 1)
                ordered_sentence.insert(int(char) - 1, word)
                print('\"{}\" inserted into position {} of ordered_sentence'.format(word, int(char) - 1))
                print(" ".join(ordered_sentence))
                break

    return " ".join(ordered_sentence)


print(order('is2 Thi1s T4est 3a'))
print(order('4of Fo1r pe6ople g3ood th5e the2'))
print(order('d4o dru7nken sh2all w5ith s8ailor wha1t 3we a6'))
print(order(' 6 4 2 8 7 5 1 9 3'))
print(order(''))
