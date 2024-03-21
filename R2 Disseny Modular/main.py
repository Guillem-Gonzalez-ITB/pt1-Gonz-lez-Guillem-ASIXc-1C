"""
Adriana Sánchez
Guillem González Rodríguez
ASIXc 1C
21/3/2024


main.py
La seva funcionalitat és obtenir les dades, processar-les per a obtenir
les “paraules boges” i finalment mostrar-les per pantalla

crazy_words.py
És “qui sap”, és a dir, té implementada la lògica necessària
per a convertir un text de paraules “normals”, en un text de “paraules boges”.

data_source.py
És l’encarregada d’obtenir les dades.
En aquesta versió les demanarà per teclat.
Tot i que és probable, que en posteriors versions, demani les dades per fitxer.
"""

import crazy_words


# region main
def main():
    sentence = str(crazy_words.get_string())
    crazy_words.split_words(sentence)
    crazy_words.mix_letters(crazy_words.churro)

# endregion


main()
