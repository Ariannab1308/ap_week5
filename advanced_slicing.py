def advanced_slice():
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