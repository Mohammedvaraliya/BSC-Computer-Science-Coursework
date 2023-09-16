def encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)  # Encrypt uppercase characters
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)  # Encrypt lowercase characters
        else:
            result += char  # Leave non-alphabet characters unchanged

    return result

def decrypt(encrypted_text, s):
    decrypted_result = ""

    for i in range(len(encrypted_text)):
        char = encrypted_text[i]

        if char.isupper():
            decrypted_result += chr(((ord(char) - s - 65) + 26) % 26 + 65)  # Decrypt uppercase characters
        elif char.islower():
            decrypted_result += chr(((ord(char) - s - 97) + 26) % 26 + 97)  # Decrypt lowercase characters
        else:
            decrypted_result += char  # Leave non-alphabet characters unchanged

    return decrypted_result

if __name__ == "__main__":
    text = input("Enter the text to encrypt: ")
    s = 3
    print("Text: " + text)

    encrypted_text = encrypt(text, s)
    print("Cipher: " + encrypted_text)

    decrypted_text = decrypt(encrypted_text, s)
    print("Decrypted Text: " + decrypted_text)
