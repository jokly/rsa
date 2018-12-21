import random
import json
import base64
import sympy as sp
from vars import dh_g, dh_p
from utils import prime_with, msg_hash, modinv, xor

def diffie_hellman_alice():
    g = dh_g()
    p = dh_p()

    a = random.randint(2**64, 2**128)
    A = pow(g, a, p)

    print('A: ', A)
    
    B = int(input('Enter B:').strip())
    K = pow(B, a, p)
    
    print('K: ', K)

    return K

def keygen():
    p = sp.randprime(17, 2 ** 16)
    g = random.randint(0, 2 ** 32)
    k = p - 1

    while pow(g, k, p) != 1:
	    g += 1

    x = sp.randprime(2, p - 1)
    y = pow(g, x, p)

    return (g, p, y, x)

def sign(msg, g, p, x):
    m = msg_hash(msg)
    k = prime_with(p - 1)
    r = pow(g, k, p)
    s = ((m - x * r) * modinv(k, p - 1)) % (p - 1)

    return (r, s)

def encrypt_and_sign(msg, k):
	(g, p, y, x) = keygen()
	(r, s) = sign(msg, g, p, x)
	content = json.dumps((msg, g, p, y, r, s))
	encrypted = xor(content, str(k)).encode('ascii')

	return base64.b64encode(encrypted)

if __name__ == "__main__":
    K = diffie_hellman_alice()
    msg = input('Input message to encrypt: ').strip()

    encrypted = encrypt_and_sign(msg, K)
    print(encrypted)
