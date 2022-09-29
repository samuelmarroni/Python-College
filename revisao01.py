from random import randint

L = []
for i in range(10):
    L.append(randint(1, 50))
print(L)
M = sorted(L)

p1 = L.index(M[9])
p2 = L.index(M[8])
print(f"Valor {M[9]}, {M[8]}, posição {p1}, {p2}")
