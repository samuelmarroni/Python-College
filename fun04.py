def primo(num):
    mult = 0
    for i in range(2, num):
        if (num % i == 0):
            mult += 1
    return mult == 0

num = int(input("Informe um número: "))
if primo(num):
    print("Primo!")
else:
    print("Não é primo!")
