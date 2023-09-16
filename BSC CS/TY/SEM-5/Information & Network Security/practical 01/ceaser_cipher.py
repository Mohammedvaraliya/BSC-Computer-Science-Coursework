def encrypt(text,s):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65) # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result



if __name__ == "__main__":
    
    text=input(" Enter the text to encrypt ")
    s = 3
    print("Text : " + text)
    str(s)
    print( "Cipher: " + encrypt(text,s))