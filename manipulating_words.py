def manipulate_words(): 
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