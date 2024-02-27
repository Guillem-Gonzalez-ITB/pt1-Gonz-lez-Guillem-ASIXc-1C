import random
import re

def desordenar_palabra(palabra):
    letras = [letra for letra in palabra[1:-1] if letra.isalpha()] # Guarda solo las letras de la palabra
    random.shuffle(letras)
    palabra_desordenada = palabra[0] + ''.join(letras) + palabra[-1] # Mantiene la primera y última letra, e inserta las letras desordenadas
    return palabra_desordenada

def desordenar_frase(frase):
    palabras_y_especiales = re.findall(r"[\w']+|[^\w\s]", frase) # Encuentra todas las palabras y los caracteres especiales
    frase_desordenada = ''
    for elemento in palabras_y_especiales:
        if elemento.isalpha(): # Si es una palabra, la desordenamos
            palabra_desordenada = desordenar_palabra(elemento)
            frase_desordenada += palabra_desordenada + ' ' # Añadimos un espacio después de cada palabra desordenada
        else: # Si es un caracter especial, lo añadimos directamente
            frase_desordenada += elemento
    return frase_desordenada

frase = input("Introduce una frase: ")
frase_desordenada = desordenar_frase(frase)
print("Frase desordenada:", frase_desordenada)
