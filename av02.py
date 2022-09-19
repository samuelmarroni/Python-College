#Felipe Garbelini Ferreira 	        R.A.:624421
#Gabriel Gomes Batista Nunes 	    R.A.:624403
#Samuel Icaro Marroni               R.A.:623989
#Gabriel Nicoletti                  R.A.:607711

def validaNumero(n):
    if (n < 1000 or n > 9999 ):
        print("Número inválido.")
        return False
    
    separados = []
    for i in range(4):
        n1 = n % 10
        separados.append(n1)
        n //= 10
        
    if (separados[0] == separados[1] and separados[1] == separados[2] and separados[2] == separados[3]):
        return False
    
    return True

def crescente(n):
    separados = []
    for i in range(4):
        n1 = n % 10
        separados.append(n1)
        n //= 10
    separados.sort()

    mult = 1000
    crescente = 0
    for i in range (4):
        crescente += separados[i] * mult
        mult = mult // 10 
    return crescente

def decrescente(n):
    separados = []
    for i in range(4):
        n1 = n % 10
        separados.append(n1)
        n //= 10
    separados.sort(reverse=True)
    mult = 1000
    decrescente = 0
    for i in range (4):
        decrescente += separados[i] * mult
        mult = mult // 10 
    return decrescente

n = int(input("Informe um número de no mínimo 4 digitos, com pelo menos 2 digitos distintos: "))

if validaNumero(n):
    numeroCrescente = crescente(n)
    numeroDecrescente = decrescente(n)
    
    subtracao = numeroDecrescente
    print(n)
    while True:
        subtracao = numeroDecrescente - numeroCrescente
        print(subtracao)
        if (subtracao == 6174):
            break
        numeroCrescente = crescente(subtracao)
        numeroDecrescente = decrescente(subtracao)
else:
    print("Número inválido")
