def anoBissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    return False

def validaData(data):
    data = data.split('/')
    dia = int(data[0])
    mes = int(data[1])
    ano = int(data[2])
    
    if mes < 1 or mes > 12:
        return False
    
    if mes == 2:
        if anoBissexto(ano):
            if dia < 1 or dia > 29:
                return False
        if dia > 28:
            return False
    
    dias31 = [1, 3, 5, 7, 8, 10, 12]
    dias30 = [4, 6, 9, 11]
    
    if mes in dias31:
        if dia > 31 or dia < 1:
            return False
    if mes in dias30:
        if dia > 30 or dia < 1:
            return False
        
    return True

data = input("Informe uma data >>")
if validaData(data):
    print("Data válida")
else:
    print("Data inválida")
