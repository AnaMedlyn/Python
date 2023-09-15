#Escreva uma função chamada "contador_vogais" que recebe uma string como parâmetro e retorna
#o número de vogais na string.

def contadorVogais(palavra):
    vogais = "aeiouAEIOU"
    qtdVogais = 0
    
    for letra in palavra:
        if letra in vogais:
            qtdVogais += 1
            
    return qtdVogais

palavra = input("Digite a palavra: ")
print (contadorVogais(palavra))
