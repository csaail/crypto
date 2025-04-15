#!pip install stegano
#P5 Steganography

from stegano import lsb

# Hide message in image
steg = lsb.hide('/content/flower.jpg', 'Flower is blue')
steg.save('/content/flower-secret.jpg')

# Retrieve hidden message
msg = lsb.reveal('D:/salma/flower-secret.png')
print(msg)
