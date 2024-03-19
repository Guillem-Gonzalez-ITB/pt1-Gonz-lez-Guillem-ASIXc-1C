import crazy_words


# region main
def main():
    sentence = crazy_words.get_string()
    crazy_words.split_words(sentence)
    crazy_words.mix_letters(crazy_words.churro)

# endregion


main()
