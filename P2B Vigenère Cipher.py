#P2B Vigenere Cipher

import numpy as np

# Encryption
def encrypt_words(plain_text, key):
    cipher_text = ''
    n = len(plain_text)
    ceil_val = int(np.math.ceil(n / len(key)))
    key = (key * ceil_val)[:n]

    for i in range(n):
        if plain_text[i].isupper():
            pi = ord(plain_text[i]) - 65
            ki = ord(key[i]) - 65
            ei = (pi + ki) % 26
            cipher_text += chr(65 + ei)
        else:
            pi = ord(plain_text[i]) - 97
            ki = ord(key[i]) - 97
            ei = (pi + ki) % 26
            cipher_text += chr(97 + ei)

    print('Encrypted Text:', cipher_text)
    return cipher_text

# Decryption
def decrypt_words(cipher_text, key):
    plain_text = ''
    n = len(cipher_text)
    ceil_val = int(np.math.ceil(n / len(key)))
    key = (key * ceil_val)[:n]

    for i in range(n):
        if cipher_text[i].isupper():
            ei = ord(cipher_text[i]) - 65
            ki = ord(key[i]) - 65
            di = (ei - ki)
            if di >= 0:
                di = di % 26
            else:
                di = (di + 26) % 26
            plain_text += chr(65 + di)
        else:
            ei = ord(cipher_text[i]) - 97
            ki = ord(key[i]) - 97
            di = (ei - ki)
            if di >= 0:
                di = di % 26
            else:
                di = (di + 26) % 26
            plain_text += chr(97 + di)

    print('Decrypted Text:', plain_text)


# Main
plain_text = input('Enter the plain text to be encrypted and decrypted: ')
key = input('Enter the key for Vigenere cipher: ')
cipher_text = encrypt_words(plain_text, key)
decrypt_words(cipher_text, key)
