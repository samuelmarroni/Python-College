from random import randint

def verifi(lst, d):
    if lst[0] == d:
        return True
    elif len(lst) > 1:
        return verifi(lst[1:], d)
    else:
        return False

lista = []
for i in range(10):
    lista.append(randint(1, 50))
print(lista)
valor = int(input("Digite um valor: "))
if verifi(lista, valor):
    print("Verdadeiro")
else:
    print("Falso")
