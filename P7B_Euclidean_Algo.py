#P7B Euclidean Algo

def gcd(a, b):
    temp = 0
    while True:
        temp = a % b
        if temp == 0:
            return b
        a = b
        b = temp

# User Input
a = int(input("Enter a value of a: "))
b = int(input("Enter a value of b: "))

# Output GCD
print("GCD of", a, ",", b, "is", gcd(a, b))
