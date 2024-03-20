import random
import data_source

SEPARATORS = ["¡", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "¿",
              "?", "@", "[", "\\", "]", "^", "_", "{", "|", "}", "~", " ",
              "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

churro = []
frase = []

# region definición de funciones ------------


def get_string():
    data_source.get_data__from_keyboard()


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

# endregion
