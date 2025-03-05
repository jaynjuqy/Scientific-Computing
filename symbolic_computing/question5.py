#JKUAT cybersecurity engineers are designing a public key encryption system that uses prime numbers. 
#The encryption follows the equation:
#   C = P^e % N
#       where C is the ciphertext, P is the plaintext, e is the encryption key and N is the public modulus

import sympy as sp

P, e, N = 7, 3, 33
#Task 1: Define a symbolic function for the encryption process
def encrypt(plain_text, encryption_key, modulus):
    cipher_text = pow(plain_text, encryption_key, modulus)
    return cipher_text

#Task 2: compute the modular inverse of P to decrypt the message
def decrypt(plain_text, modulus):
    p_inverse = sp.mod_inverse(plain_text, modulus)
    return p_inverse

#Task 3: if P = 7, e = 3 and N = 33, compute the ciphertext
print(f"The ciphertext of P {P} is {encrypt(P, e, N)}")

print(f"The modular inverse of P {P} is {decrypt(P, N)}")
