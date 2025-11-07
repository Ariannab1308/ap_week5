def join_split():
    # String Joining and Splitting:
    # Given the list motto = ["Make", "haste", "slowly."],
    # a. Convert the list into a single string.
    motto = ["Make", "haste", "slowly."]
    motto_string = ' '.join(motto)
    print(motto_string)
    # b. Now, split the string at every occurrence of the letter 'a'.
    split_motto = motto_string.split('a')
    print(split_motto)