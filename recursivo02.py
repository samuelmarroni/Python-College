def potencia(num, elev):
    if elev == 1:
        return elev
    return num * potencia(num, elev - 1)

num = int(input("Numero >> "))
elev = int(input("Elevação >> "))
print(potencia(num, elev))
