# Solicita ao usuário para inserir um número
numero = int(input("Insira um número: "))

# Inicializa o fatorial como 1
fatorial = 1

# Inicializa um contador
contador = 1

# Loop while para calcular o fatorial
while contador <= numero:
    fatorial *= contador
    contador += 1

# Imprime o resultado
print(f"O fatorial de {numero} é {fatorial}")