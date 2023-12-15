def rail_fence_encrypt(text, rails):
    text = ''.join([''.join(char) for char in text]).replace(" ", "") # Remove spaces
    fence = [[' ' for _ in range(len(text))] for _ in range(rails)]
    direction = -1  # Direction to move along the rails (up or down)
    row, col = 0, 0  # Initial position on the rail fence

    for char in text:
        fence[row][col] = char
        if row == 0 or row == rails - 1:
            direction *= -1  # Change direction at the top or bottom rail
        row += direction
        col += 1

    encrypted_text = ''.join([''.join(row) for row in fence]).replace(" ", "")  # Remove spaces
    return encrypted_text

def rail_fence_decrypt(encrypted_text, rails):
    fence = [[' ' for _ in range(len(encrypted_text))] for _ in range(rails)]
    direction = -1  # Direction to move along the rails (up or down)
    row, col = 0, 0  # Initial position on the rail fence

    for _ in range(len(encrypted_text)):
        fence[row][col] = 'X'  # Mark the positions on the fence
        if row == 0 or row == rails - 1:
            direction *= -1  # Change direction at the top or bottom rail
        row += direction
        col += 1

    decrypted_text = ''
    text_index = 0

    for row in range(rails):
        for col in range(len(encrypted_text)):
            if fence[row][col] == 'X':
                fence[row][col] = encrypted_text[text_index]
                text_index += 1

    direction = -1  # Reset the direction for reading
    row, col = 0, 0

    for _ in range(len(encrypted_text)):
        decrypted_text += fence[row][col]
        if row == 0 or row == rails - 1:
            direction *= -1  # Change direction at the top or bottom rail
        row += direction
        col += 1

    return decrypted_text

if __name__ == "__main__":
    text = input("Enter the text to encrypt: ")
    rails = int(input("Enter the number of rails: "))

    encrypted_text = rail_fence_encrypt(text, rails)
    print("Cipher: " + encrypted_text)

    decrypted_text = rail_fence_decrypt(encrypted_text, rails)
    print("Decrypted Text: " + decrypted_text)
