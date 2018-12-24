import numpy as np
import sympy as sp
from itertools import cycle

def read_int(reader):
    return int.from_bytes(reader.read(32), byteorder='big')

def coprime(n):
	m = sp.randprime(2 ** 16, 2 ** 32)
	while np.gcd(m, n) != 1:
		m = sp.randprime(2 ** 16, 2 ** 32)

	return m

def prime_with(p):
    k = sp.randprime(2, p)
    while np.gcd(k, p) != 1:
        k = sp.randprime(2, p)
    
    return k

def msg_hash(msg):
	v = 10
	for i in range(len(msg)):
		v = (v * (ord(msg[i]) + v + i)) % 2 ** 32

	return v

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	g, y, x = egcd(b % a, a)
	return (g, x - (b // a) * y, y)

def modinv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		assert(0)
	return x % m

def xor(msg, key):
	return ''.join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(msg, cycle(key))])
