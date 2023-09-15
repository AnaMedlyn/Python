#Modificar elementos de uma lista:
    
frutas = ["Maça","Banana", "Manga", "Pera"]

frutas[1] = "Abacaxi"

print(frutas)

##################################

frutas = ["Maçã", "Banana", "Manga", "Pera"]

fruta_antiga = "Banana"
nova_fruta = "Abacate"

for i in range(len(frutas)):
    if frutas[i] == fruta_antiga:
        frutas[i] = nova_fruta

print(frutas)


