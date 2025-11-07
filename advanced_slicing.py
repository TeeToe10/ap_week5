def advanced_slice():
    # Advanced Slicing:
    # Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # a. Extract the letters 'hij'.
    print(alphabet[7:10])
    hij_index = alphabet.index('hij') # Index of substring
    print(hij_index) # 7
    # b. Extract every second letter starting from 'a' to 'm'.
    print(alphabet[0:13:2])
    # c. Reverse the entire string using slicing.
    print(alphabet[: : -1]) #reversing a string

