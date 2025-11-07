def problem2():
    # Problem Set 2: Extracting Information
    # From Descriptions:
    # Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
    info = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
    name = info.split(" - ")[-1]
    print(name)
    # Manipulating Words:
    # Given the string info = "Python is fun. Fun is good. Good is subjective.",
    quote = "Python is fun. Fun is good. Good is subjective."
    # a. Extract the word 'subjective' without knowing its exact position.
    print(quote.rfind('subjective')) 
    # b. Extract every third word.
    every_third_word = info.split()[::3]
    # c. Reverse the positions of the words, but keep the characters in each word in the same order.
    reversed_word_positions = info.split()[::-1]
    reversed_word_positions = ' '.join(reversed_word_positions)
    print(reversed_word_positions)