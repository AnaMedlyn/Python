# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

# Função para verificar se alguém ganhou
def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas, colunas e diagonais
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    if (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador) or (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador):
        return True
    return False

# Função para verificar se o tabuleiro está cheio (empate)
def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

# Função principal do jogo
def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogo_acabou = False

    while not jogo_acabou:
        exibir_tabuleiro(tabuleiro)
        print(f"É a vez do jogador {jogador_atual}.")
        linha = int(input("Digite o número da linha (0, 1 ou 2): "))
        coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            if verificar_vitoria(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f"O jogador {jogador_atual} venceu!")
                jogo_acabou = True
            elif verificar_empate(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print("O jogo empatou!")
                jogo_acabou = True
            else:
                jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Essa posição já está ocupada. Tente novamente.")

# Iniciar o jogo
jogo_da_velha()