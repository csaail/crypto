#P2C Affine Cipher

# Affine Cipher Encryption
def encrypt_words(plain_text, a, b):
    cipher_text = ''
    for word in plain_text:
        for i in word:
            if i.isupper():
                val = ord(i) - 65
                cal = ((a * val) + b) % 26
                enc_word = chr(65 + cal)
            else:
                val = ord(i) - 97
                cal = ((a * val) + b) % 26
                enc_word = chr(97 + cal)
            cipher_text += enc_word
    print('Encrypted Text:', cipher_text)
    return cipher_text

# Affine Cipher Decryption
def decrypt_words(cipher_text, a, b):
    plain_text = ''

    # Find modular inverse of a under mod 26
    c = 0
    for i in range(1, 27):
        if (a * i) % 26 == 1:
            c = i
            break

    for word in cipher_text:
        for i in word:
            if i.isupper():
                val = ord(i) - 65
                cal = (c * (val - b)) % 26
                dec_word = chr(65 + cal)
            else:
                val = ord(i) - 97
                cal = (c * (val - b)) % 26
                dec_word = chr(97 + cal)
            plain_text += dec_word
    print('Decrypted Text:', plain_text)

# Main
plain_text = input('Enter the plain text to be encrypted & decrypted: ').split()
a = int(input('Enter the key for a: '))
b = int(input('Enter the key for b: '))

cipher_text = encrypt_words(plain_text, a, b)
decrypt_words(cipher_text, a, b)
