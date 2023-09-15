# Loop for para percorrer os números de 1 a 100
for numero in range(1, 101):
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

    # Se for primo, imprime o número
    if e_primo:
        print(numero)
        