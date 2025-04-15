# P2 Shift Cipher / Caeser Cipher

# Encryption function
def encrypt_words(plain_text, key):
    cipher_text = ''
    for word in plain_text:
        for i in word:
            if i.isupper():
                val = ord(i) - 65
                enc_word = chr(65 + (val + key) % 26)
            else:
                val = ord(i) - 97
                enc_word = chr(97 + (val + key) % 26)
            cipher_text += enc_word
    print('Encrypted Text:', cipher_text)
    return cipher_text

# Decryption function
def decrypt_words(cipher_text, key):
    plain_text = ''
    for word in cipher_text:
        for i in word:
            if i.isupper():
                val = ord(i) - 65
                dec_word = chr(65 + (val - key) % 26)
            else:
                val = ord(i) - 97
                dec_word = chr(97 + (val - key) % 26)
            plain_text += dec_word
    print('Decrypted Text:', plain_text)

# Main program
plain_text = input('Enter the plain text to be encrypted & decrypted: ').split()
key = int(input('Enter the key for Shift Cipher: '))

cipher_text = encrypt_words(plain_text, key)
decrypt_words(cipher_text, key)