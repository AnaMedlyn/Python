altura = 7
largura = altura * 2 - 1

for i in range(1, altura + 1):
    espacos = " " * ((largura - (2 * i - 1 )) // 2)
    asteriscos = "*" * (2 * i - 1)
    linha = espacos + asteriscos + espacos
    print(linha)