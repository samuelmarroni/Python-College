def potencia(base, expoente):
    potencia = base
    for i in range(expoente-1):
        potencia *= base
    print(f"Potência: {potencia}")

base = int(input("Informe a base: "))
expoente = int(input("Informe o expoente: "))
potencia(base, expoente)
