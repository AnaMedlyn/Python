#Escreva uma função chamada "fatorial" que recebe um número inteiro como parâmetro e retorna o
#fatorial desse número. O fatorial de um número n é o produto de todos os números inteiros de 1 a n.

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

numero = int(input("Digite um número inteiro: "))
resultadoFatorial = fatorial(numero)
print("O fatorial de", numero, "é", resultadoFatorial)

#Ou

def calculaFatorial (numero):
    resultado = 1
    for i in range (1, numero):
        resultado *= i
    return resultado
    
numero = int(input("digita um numero"))
print(calculaFatorial(numero))