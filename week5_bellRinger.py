# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
from cmath import phase


magic = 'abracadabra'
# a. Retrieve the 5th character.
print(magic[4])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
print(magic.find("c"))

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
print(reversed_wordpositions)

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
phrase1 = "MAY THE FORCE BE WITH YOU"
print("phrase1 Lowercase:", phrase1.lower())
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
motto = ["Make", "haste", "slowly."]
sentence = " ".join(motto)
split_sentence = sentence.split('a')
# b. Now, split the string at every occurrence of the letter 'a'.
print(split_sentence)   ['M', 'ke h', 'ste slowly.']
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
sentence =  "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
sentence2 = sentence.replace("busy", "distracted")
print(sentence2)
# b. Replace "plans" with "mistakes".
sentence3 = sentence.replace("plans","mistakes")
print(sentence3)

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.