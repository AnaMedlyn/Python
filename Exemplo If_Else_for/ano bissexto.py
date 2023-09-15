def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

# Solicita ao usuário que insira um número de ano
ano = int(input("Insira um ano: "))

# Verifica se o ano é bissexto e imprime a mensagem correspondente
if eh_bissexto(ano):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")