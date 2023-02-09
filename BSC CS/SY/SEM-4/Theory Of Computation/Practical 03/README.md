Aim : Write a program for tokenization of given input.

    The tokenize function takes a string input_str as input.

    It initializes two variables, tokens which is an empty list that will store the individual tokens,
    and word which is an empty string that will store the current word as it is being built.

    The code then uses a for loop to iterate over each character in input_str. For each character:

        a. If the character is either alphanumeric (i.e., it is either a letter or a digit) or a letter,
           the character is added to the current word by appending it to the end of the string.

        b. If the character is not alphanumeric or a letter, it is considered to be a delimiter between 
           words. In this case, the current word is added to the tokens list if it is not empty, and 
           the word variable is reset to an empty string.

    After the for loop has finished, if the word variable is not empty, it is added to the tokens list.

    The function returns the tokens list.