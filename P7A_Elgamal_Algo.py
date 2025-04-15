#P7A Elgamal_Algo

# Key & Cipher Generators
def generate_e2():
    e2 = pow(e1, d, p)
    return e2

def generate_c1():
    c1 = pow(e1, r, p)
    return c1

def generate_c2():
    c2 = (pt * pow(e2, r, p)) % p
    return c2

# Encryption Function
def encryption():
    ct = (c1, c2)
    return ct

# Decryption Function
def decryption():
    temp = pow(c1, d, p)  # temp = c1^d mod p
    temp_inv = None
    for i in range(1, p):
        if (temp * i) % p == 1:
            temp_inv = i
            break
    dpt = (c2 * temp_inv) % p
    return dpt

# User Input
p = int(input("Enter 1st part of public key (prime p): "))
e1 = int(input("Enter 2nd part of public key (primitive root e1): "))
d = int(input("Enter the private key d: "))
r = int(input("Enter a random integer r: "))
pt = int(input("Enter the plain text (number): "))

# Generation
e2 = generate_e2()
c1 = generate_c1()
c2 = generate_c2()

# Output
print("Encrypted Text:", encryption())
print("Decrypted Text:", decryption())
