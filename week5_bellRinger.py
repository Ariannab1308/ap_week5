# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic = "abracadabra"
# a. Retrieve the 5th character.
fifth_character = magic[4]
print(fifth_character)
# b. Retrieve the second to last character.
second_to_last_character = magic[-2]
print(second_to_last_character)
# c. Find the first occurrence of the letter 'c'.
magic = 'abracadabra'
index_of_c = magic.find('c')
print(index_of_c)

# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
extract_hij = alphabet[7:10] 
print(f"Extracted 'hij': {extract_hij}")
# b. Extract every second letter starting from 'a' to 'm'.
every_second_letter = alphabet[0:13:2]
print(f"Every second letter from 'a' to 'm': {every_second_letter}")
# c. Reverse the entire string using slicing.
reversed_string = alphabet[::-1]
print(f"Reversed string: {reversed_string}")

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(quote[83:99])

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
info = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
print(info.rfind('subjective'))
subjective_word = info[36:46]
print(subjective_word)
# b. Extract every third word.
every_third_word = info.split() [::3]
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
reversed_word_positions = info.split() [::-1]
reversed_word_positions = ' '.join(reversed_word_positions)
print(reversed_word_positions)


# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
text = "MAY THE FORCE BE WITH YOU."
lowercase_text = text.lower()
print(lowercase_text)

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
motto = ["Make", "haste", "slowly."]
motto_string = ''.join[motto]
print(motto_string)
# b. Now, split the string at every occurrence of the letter 'a'.
split_motto = motto_string.split('a')
print(split_motto)


# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
sentence = "Life is what happens when you are busy making other plans."
modified_scentence = sentence.replace("busy", "distracted").replace("plans", "mistakes")

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
word = "moonlight"
quote = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
appears_in_quote = word in quote 
print(appears_in_quote)

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
phrase =  "Supercalifragilisticexpialidocious"
length_of_phrase = len(phrase)
# b. Count the number of times the letter 'i' appears in the same word/phrase.
count_of_i = phrase.count ('i')
print (count_of_i)