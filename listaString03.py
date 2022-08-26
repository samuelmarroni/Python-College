# Faça um programa em Python que leia uma String e um caractere. Informe a quantidade de vezes que o caractere aparece na string (podendo ser maiúscula ou minúscula).

from unidecode import unidecode

frase = unidecode(input("Informe uma frase:").upper())
caracter = unidecode(input("Informe uma letra:").upper())

count = 0
for i in range(len(frase)):
    if (frase[i] == caracter):
        count += 1

print(f"O caracter {caracter} aparece {count} vezes")
