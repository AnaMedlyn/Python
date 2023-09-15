#Declararando listas em Python:

valores = [x** 2 for x in range (1,6)]
print(valores)


################################

valores = []

for x in range(1, 6):
    valor_quadrado = x ** 2
    valores.append(valor_quadrado)
    
print(valores)

