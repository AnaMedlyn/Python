lista = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def encontrarDiagonalPrincipal(lista):
    resultado = 0
    for i in range(0,len(lista)):
        for j in range(0,len(lista)):
            if i == j:
                resultado += lista[i][j]
    return resultado

def encontrarDiagonalSecundaria(lista):
    resultado = 0
    for i in range(0,len(lista)):
        for j in range(0,len(lista)):
            if i + j == len(lista) - 1 : #ou  if i + j == 2:
                resultado += lista[i][j]
    return resultado
                
print(encontrarDiagonalSecundaria(lista))