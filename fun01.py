def parOuImpar(num):
    if num == 0:
        print("Nulo.")
    elif num % 2 == 0:
        print("Par.")
    else:
        print("Ímpar.")

num = int(input("Informe um número: "))
parOuImpar(num)
