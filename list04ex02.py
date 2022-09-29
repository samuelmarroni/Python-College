from random import randint

L = []
M = []
T = []
for i in range(10):
    L.append(randint(1, 50))
    M.append(randint(1, 50))
    T.append(L[i])
    T.append(M[i])
print(L)
print(M)
print(T)
