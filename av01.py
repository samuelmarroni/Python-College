# Samuel Icaro Marroni | RA: 623989
# Gabriel Gomes Batista Nunes | RA: 624403
# Felipe Garbelini Ferreira | RA: 624421
# Breno Ryuky Funo Nakamura | RA: 626953

texto = input("Informe um texto/frase >>").lower()

pontuacoes = [".",  ",",  ":",  ";",  "!",  "?"]
for i in pontuacoes:
    texto = texto.replace(i, ' ')

texto = texto.split()
palindromos = []
for palavra in texto:
    if (len(palavra) >= 3):
        if palavra == palavra[::-1] and palavra not in palindromos:
            palindromos.append(palavra)
            print(f"{palavra} {texto.count(palavra)}")
