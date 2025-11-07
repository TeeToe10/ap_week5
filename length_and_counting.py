def length_count():
    # Length and Count:
    # a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
    # b. Count the number of times the letter 'i' appears in the same word/phrase.
    phrase = 'Supercalifragilisticexpialidocious'
    length_of_phrase = len(phrase)
    print(f"Length of the phrase: {length_of_phrase}\n")
    count_of_i = phrase.count('i')
    print(f"The letter 'i' appears {count_of_i} times in the phrase.\n")