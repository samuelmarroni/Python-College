def entrada():
    while True:
        cpf = input('CPF >> (entre com apenas números) >> ')
        if cpf.isdigit() and len(cpf) == 11:
            return cpf
        print('Entrada inválida. Digite apenas números e 11 dígitos')

def calcDigitos(cpf):
    d1 = 0
    d2 = 0
    for i in range(9):
        d1 += int(cpf[i]) * (i+1)
        d2 += int(cpf[i]) * (9-i)
    d1 %= 11
    d2 %= 11
    if d1 == 10:
        d1 = 0
    if d2 == 10:
        d2 = 0
    return d1, d2

def validaCPF(cpf, d1, d2):
    if int(cpf[9]) == d1 and int(cpf[10]) == d2:
        print('CPF válido!!')
    else:
        print('CPF inválido!!')

CPF = entrada()
dig1, dig2 = calcDigitos(CPF)
validaCPF(CPF, dig1, dig2)
