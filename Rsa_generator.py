'''import random


def encrypt_plaintext(plaintext):
    # Generate a random symmetric key
    symmetric_key = generate_symmetric_key()

    # Encrypt the plaintext using the symmetric key
    ciphertext = symmetric_encrypt(plaintext, symmetric_key)

    # Encrypt the symmetric key using the public key
    encrypted_key = rsa_encrypt(symmetric_key)

    # Store the ciphertext in a file
    store_ciphertext(ciphertext)

    # Store the encrypted key in another file
    store_encrypted_key(encrypted_key)


def generate_symmetric_key():
    # Generate a random symmetric key
    key = random.randint(0, 255)
    return key


def symmetric_encrypt(plaintext, key):
    # Encrypt the plaintext using the symmetric key
    ciphertext = ""
    for char in plaintext:
        encrypted_char = chr(ord(char) ^ key)
        ciphertext += encrypted_char
    return ciphertext


def rsa_encrypt(key):
    # Read the public key from the file
    with open('public_key.txt', 'r') as file:
        public_key = file.read()

    # Encrypt the symmetric key using the public key
    encrypted_key = ""
    for char in key:
        encrypted_char = chr(ord(char) ^ int(public_key))
        encrypted_key += encrypted_char
    return encrypted_key


def store_ciphertext(ciphertext):
    # Store the ciphertext in a file
    with open('ciphertext.txt', 'w') as file:
        file.write(ciphertext)


def store_encrypted_key(encrypted_key):
    # Store the encrypted key in a file
    with open('encrypted_key.txt', 'w') as file:
        file.write(encrypted_key)


plaintext = "Hello, World!"
encrypt_plaintext(plaintext)'''
import random


def generate_rsa_keys():
    # Генерация двух простых чисел p и q
    p = generate_prime_number()
    q = generate_prime_number()

    # Вычислить n = p * q
    n = p * q

    # Вычислить функцию Эйлера phi(n)
    phi_n = (p - 1) * (q - 1)

    # Выбор публичной экспоненты e
    e = choose_public_exponent(phi_n)

    # Вычислить частную экспоненту d
    d = compute_private_exponent(e, phi_n)

    # Store the public key (e, n) in a file
    store_public_key(e, n)

    # Store the private key (d, n) in another file
    store_private_key(d, n)


def generate_prime_number():
    # Generate a random number and check if it is prime
    while True:
        num = random.randint(2, 1000)
        if is_prime(num):
            return num


def is_prime(num):
    # Check if a number is prime
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def choose_public_exponent(phi_n):
    # Choose a public exponent e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    while True:
        e = random.randint(2, phi_n - 1)
        if gcd(e, phi_n) == 1:
            return e


def gcd(a, b):
    # Compute the greatest common divisor of two numbers
    while b != 0:
        a, b = b, a % b
    return a


def compute_private_exponent(e, phi_n):
    # Compute the private exponent d such that d * e ≡ 1 (mod phi(n))
    d = extended_euclidean_algorithm(e, phi_n)
    return d


def extended_euclidean_algorithm(a, b):
    # Compute the private exponent d using the extended Euclidean algorithm
    if b == 0:
        return 1, 0
    else:
        x, y = extended_euclidean_algorithm(b, a % b)
        return y, x - (a // b) * y


def store_public_key(e, n):
    # Store the public key (e, n) in a file
    with open('public_key.txt', 'w') as file:
        file.write(f"Public Key (e, n): ({e}, {n})")


def store_private_key(d, n):
    # Store the private key (d, n) in a file
    with open('private_key.txt', 'w') as file:
        file.write(f"Private Key (d, n): ({d}, {n})")


generate_rsa_keys()
