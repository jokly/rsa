import random
import json
import base64
from vars import dh_g, dh_p
from utils import msg_hash, xor

def diffie_hellman_bob():
    g = dh_g()
    p = dh_p()

    b = random.randint(2**64, 2**128)
    B = pow(g, b, p)

    print('B: ', B)

    A = int(input('Enter A:').strip())
    K = pow(A, b, p)

    print('K: ', K)

    return K

def check(msg, g, p, y, r, s):
    if r >= p or r <= 0 or s <= 0 or s >= p - 1:
	    return False

    m = msg_hash(msg)
    return ((pow(y, r) * pow(r, s)) % p) == pow(g, m, p)

def decrypt(msg, k):
    encrypted = base64.b64decode(msg).decode('ascii')
    content = xor(encrypted, str(k))
    (msg, g, p, y, r, s) = json.loads(content)
    isValid = check(msg, g, p, y, r, s)

    print('Signature is valid:', isValid)
    if isValid:
	    print('Message:', msg)

if __name__ == "__main__":
    K = diffie_hellman_bob()
    msg = input('Input message to decrypt: ').strip()
    decrypt(msg, K)
