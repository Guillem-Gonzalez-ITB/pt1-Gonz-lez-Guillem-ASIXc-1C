"""
Guillem González Rodríguez
ASIXc 1C
6/2/2024


Implementar en Python un programa que demani una frase per teclat i la retorni per pantalla amb les lletres de cada
paraula de la frase desordenada, tal com diu l’estudi de la Universitat de Cambridge.
"""

import random

SEPARATORS = ["¡", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "¿",
              "?", "@", "[", "\\", "]", "^", "_", "{", "|", "}", "~", " ",
              "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


churro = []
frase = []

# region definición de funciones ------------


def get_string():
    sentence = input("Introduce una frase: ")
    return sentence


def split_words(sentence):
    global frase
    c = 0
    for letter in sentence:
        c += 1

        if letter not in SEPARATORS:
            frase.append(letter)

        else:
            churro.append(frase)
            frase = [letter]
            churro.append(frase)
            frase = []

        if c == len(sentence):
            churro.append(frase)
            return churro


def mix_letters(churro):
    for m in range(len(churro)):
        word = churro[m]
        if len(word) > 3:
            print(word[0] + "".join(random.sample(word[1:-1], len(word[1:-1]))) + word[-1], end="")
        else:
            print("".join(word), end="")


def main():
    sentence = get_string()
    split_words(sentence)
    mix_letters(churro)
# endregion

# region main


main()

# endregion
