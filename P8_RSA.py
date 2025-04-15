#P8 RSA

import math

# GCD function using Euclidean Algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Prime numbers
p = 3
q = 7

# Calculate n and phi
n = p * q
phi = (p - 1) * (q - 1)

# Choose e such that 1 < e < phi and gcd(e, phi) = 1
e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    else:
        e += 1

# Calculate d, the modular inverse of e
d = 0
for i in range(1, phi):
    if (e * i) % phi == 1:
        d = i
        break

# Message
msg = 12.0
print("Message data = ", msg)

# Encryption: c = (msg ^ e) % n
c = pow(int(msg), e, n)
print("Encrypted data = ", c)

# Decryption: m = (c ^ d) % n
m = pow(c, d, n)
print("Original Message Sent = ", m)
