# a function allows us to bundle code into
# reuseable blocks, making it easier to manage
# and understand. By defining functions, we can 
# avoid code duplication and enhance readability

# define a function
def problem1():
    # pass # i put pass to avoid syntax error
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

# calling the function