#P3 Cryotoanalysis

def cryptanalysis():
    cipher_text = input('Enter the cipher text for cryptanalysis: ')

    for k in range(26):  # Try all possible shift values
        plain_text = ''
        for letter in cipher_text:
            if letter == ' ':
                plain_text += letter
            else:
                c = ord(letter) - 65  # Convert to 0–25 range
                e = (c - k) % 26
                plain_text += chr(e + 65)
        print(f'With key = {k}, Decrypted Text: {plain_text}')

# Run the function
cryptanalysis()