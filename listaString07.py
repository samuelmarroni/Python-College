#Fazer um programa em Pythonpara verificar se uma determinada String é palíndrome.
# Exs.: ANA -MUSSUM –OVO

palavra = input("Palavra >>").upper()

if palavra == palavra[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndromo")
