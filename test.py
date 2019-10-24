from math import log2
'''
num1 = 2**5
print("Encrypted: ", num1 % 21)
encrypt = num1 % 21
encrypt = encrypt ** 17
print("Decrypted: ", encrypt % 21)
'''
a = 32 ** 400
b = 31 ** 300
num1 = a % (b)
print(log2(a))
print(log2(b))
print(num1)
