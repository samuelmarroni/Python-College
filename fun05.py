def primos(intervalo):
    for i in range(intervalo):
        mult = 0
        for j in range(2, i):
            if (i % j == 0):
                mult += 1
        if mult == 0:
            print(i)

intervalo = int(input("Informe o intervalo: "))
primos(intervalo)
