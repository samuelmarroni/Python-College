#Faça um programa em Python que leia uma frase e imprima quantas vogais tem esta frase. Considerar minúscula e maiúscula. 

from unidecode import unidecode
frase = unidecode(input("Insira uma frase>>").upper())

a = (frase.count('A'))
e = (frase.count('E'))
i = (frase.count('I'))
o = (frase.count('O'))
u = (frase.count('U'))

soma = a + e + i + o + u
print(f"O total de vogais é {soma}")
