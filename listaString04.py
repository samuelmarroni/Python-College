# Faça um programa em Python que leia uma String e dois caracteres. Troque todas as ocorrências do  primeiro  caractere  (podendo  ser  maiúsculo  ou  minúsculo)  pelo  segundo  e  imprima  a quantidade de vezes que o caractere foi substituído.

text = input("Texto >>").upper()
old = input("Caracter a ser substituido >>").upper()[0]
new = input("Caracter para a substituição >>").upper()[0]

c = text.count(old)
text = text.replace(old, new)

print(f'Foram realizadas {c} substituições')
print(f'Novo texto >> {text}')
