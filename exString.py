nome = input("Informe um nome completo >>").upper()
nome = nome.split()
diminutivos = nome[-1] + ', '
preposições = ['DE', 'DA', 'DOS', 'DAS']

for i in range(len(nome) - 1):
    if nome[i] not in preposições:
        diminutivos += nome[i][0] + '. '

print(diminutivos)
