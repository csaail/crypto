#!pip install pycryptodome
#P4 AES

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_file(input_file, output_file, key):

    with open(input_file, 'rb') as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted = cipher.encrypt(pad(data, AES.block_size))
    with open(output_file, 'wb') as f:
        f.write(cipher.iv + encrypted)

def decrypt_file(input_file, output_file, key):

    with open(input_file, 'rb') as f:
        iv = f.read(16)
        encrypted = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
    with open(output_file, 'wb') as f:
        f.write(decrypted)

def main():
    # Generate a random 16-byte (128-bit) AES key
    key = get_random_bytes(16)

    input_file = input("Enter the path of the input file to encrypt/decrypt: ").strip()

    encrypt_file(input_file, 'encrypt.txt', key)
    print(f"File encrypted ")

    decrypt_file('encrypt.txt', 'decrypt.txt', key)
    print(f"File decrypted ")

if __name__ == "__main__":
    main()
