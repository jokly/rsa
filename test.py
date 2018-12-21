g = 61343
m = 1468937072
p = 63650
r = 31389
s = 42507
y = 55419

a1 = ((pow(y, r) * pow(r, s)) % p)
a2 = pow(g, m, p)
print(a1)
print(a2)
print(a1 == a2)
