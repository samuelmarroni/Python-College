n = int(input("Digite um número entre 2 e 20: "))

A = [0] * n
for i in range(n):
    A[i] = [0] * n

c = 1
ini = 0
fim = n

while c <= n**2:
    for i in range(ini, fim):
        A[ini][i] = c
        c += 1
    for i in range(ini+1, fim):
        A[i][fim-1] = c
        c += 1
    for i in range(fim-2, ini-1, -1):
        A[fim-1][i] = c
        c += 1
    for i in range(fim-2, ini, -1):
        A[i][ini] = c
        c += 1

    ini += 1
    fim -= 1

for i in range(n):
    for j in range(n):
        print(f'{A[i][j]:02}', end=' ')
    print()
