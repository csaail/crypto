#!pip install bcrypt
# Salt and Hash

import bcrypt

# Get user password and prepare fake password for comparison
pwd = input('Enter the Password: ')
falsepwd = 'FalsePassword'

# Encode the passwords to bytes
bytepwd = pwd.encode('UTF-8')
bytefpwd = falsepwd.encode('UTF-8')

# Generate Salt
mySalt = bcrypt.gensalt()

# Hash the password
hash_val = bcrypt.hashpw(bytepwd, mySalt)
print('Hashed password:', hash_val)

# Check if entered password matches the hash
print('Matching hashed password with entered password:', bcrypt.checkpw(bytepwd, hash_val))
print('Matching hashed password with false password:', bcrypt.checkpw(bytefpwd, hash_val))
