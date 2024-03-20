"""
Guillem González Rodríguez
ASIXc 1C
6/2/2024


Implementar en Python un programa que demani una frase per teclat i la retorni per pantalla amb les lletres de cada
paraula de la frase desordenada, tal com diu l’estudi de la Universitat de Cambridge.
"""

import random
import string

# region definición de funciones ------------


# todo definir la función que mezcla las letras de las palabras
def mix_letters(word):
    chars = word.split()
    if is_number(word):
        print(word, end="")
        return
    # todo mezclar las letras de las palabras excepto la primera y la última
    elif len(word) > 2:
        if chars[0] in list(string.punctuation):
            if chars[-1] in list(string.punctuation):
                print(chars[0] + chars[1] + "".join(random.sample(chars[2:-2], len(word[2:-2]))) + chars[-2] + chars[-1]
                      , end="")
            else:
                print(word[0] + word[1] + "".join(random.sample(word[2:-1], len(word[2:-1]))) + word[-1], end="")

        # todo devolver la frase con las palabras modificadas
        else:
            print(word[0] + "".join(random.sample(word[1:-1], len(word[1:-1]))) + word[-1], end="")
    else:
        print(word, end="")


# todo crear un for para recorrer las palabras
def run_words(words):

    for i in range(len(words)):
        mix_letters(words[i])
        print(" ", end="")
        if i > 1 and i % 20 == 0:
            print("")


# todo identificar si es numero o no
def is_number(word):
    try:
        float(word)
        return True
    except ValueError:
        return False
# endregion

# main


sentence = input("Introduce una frase: ")
# todo dividir la frase en palabras
words = sentence.split(" ")
run_words(words)
