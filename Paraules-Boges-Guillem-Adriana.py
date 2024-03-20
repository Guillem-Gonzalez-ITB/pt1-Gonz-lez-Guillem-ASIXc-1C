"""
Adriana Sánchez
Guillem González
27/2/2024
UF2 Pt1
"""

import random

def desordenar_palabra(palabra):
    letras_intermedias = [letra for letra in palabra[1:-1] if letra.isalpha()]
    letras_desordenadas = random.sample(letras_intermedias, len(letras_intermedias))
    palabra_desordenada = palabra[0] + ''.join(letras_desordenadas) + palabra[-1]
    return palabra_desordenada

def desordenar_frase(frase):
    palabra = ''
    frase_desordenada = ''
    for caracter in frase:
        if caracter.isalnum() or caracter == "'":
            palabra += caracter
        else:
            if palabra:
                palabra_desordenada = desordenar_palabra(palabra)
                frase_desordenada += palabra_desordenada
                palabra = ''
            frase_desordenada += caracter
    if palabra:
        palabra_desordenada = desordenar_palabra(palabra)
        frase_desordenada += palabra_desordenada
    return frase_desordenada

frase = input("Introduce una frase: ")
frase_desordenada = desordenar_frase(frase)
print("Frase desordenada:", frase_desordenada)
