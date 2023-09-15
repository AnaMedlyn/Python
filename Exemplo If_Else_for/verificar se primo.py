# Solicita ao usuário para inserir um número
numero = int(input("Insira um número: "))

# Inicializa uma flag para verificar se é primo
e_primo = True

# Verifica se o número é maior que 1
if numero <= 1:
    e_primo = False
else:
    # Loop for para verificar divisibilidade
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            e_primo = False
            break

# Imprime o resultado
if e_primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")