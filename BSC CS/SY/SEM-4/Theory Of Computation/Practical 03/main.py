# Write a program for tokenization of given input.

def tokenize(input_str):
    
    tokens = []
    word = ""

    for char in input_str:
        if char.isalnum() or char.isalpha():
            word += char

        else:
            if word:
                tokens.append(word)
                word = ""
    if word:
        tokens.append(word)
        word = ""
    
    return tokens



if __name__ == "__main__":

    string = "This is an example of tokenization"
    print(tokenize(string))