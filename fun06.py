from random import randint

def maiorElementoColuna(matriz, coluna):
    maiorColuna = matriz[0][coluna]
    for i in range(10):
        for j in range(10):
            if j == coluna and matriz[i][j] > maiorColuna:
                maiorColuna = matriz[i][j]
    return maiorColuna

def menorElementoLinha(matriz, linha):
    menorLinha = matriz[linha][0]
    for i in range(10):
        for j in range(10):
            if i == linha and matriz[i][j] < menorLinha:
                menorLinha = matriz[i][j]
    return menorLinha

M = [0] * 10
for i in range(10):
    M[i] = [0] * 10
    for j in range(10):
        M[i][j] = randint(1, 50)
        print(f'{M[i][j]:02}', end=' ')
    print()

maiorColuna = maiorElementoColuna(M, 3)
menorLinha = menorElementoLinha(M, 6)
print(maiorColuna, menorLinha)
