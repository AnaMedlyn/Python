import os

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    limpar_tela()
    print("   0   1   2")
    print("0  " + " | ".join(tabuleiro[0]))
    print("  ---+---+---")
    print("1  " + " | ".join(tabuleiro[1]))
    print("  ---+---+---")
    print("2  " + " | ".join(tabuleiro[2]))

# Função para verificar se alguém ganhou
def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True

    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

# Função para verificar empate
def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

# Função principal do jogo
def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

    jogador1 = input("Nome do jogador 1 (X): ")
    jogador2 = input("Nome do jogador 2 (O): ")

    jogador_atual = jogador1
    simbolo_atual = "X"

    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"É a vez de {jogador_atual} ({simbolo_atual})")

        linha = int(input("Digite o número da linha (0, 1 ou 2): "))
        coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] != " ":
            print("Essa célula já está ocupada. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = simbolo_atual

        if verificar_vitoria(tabuleiro, simbolo_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"{jogador_atual} venceu!")
            break

        if verificar_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            break

        jogador_atual, simbolo_atual = (jogador2, "O") if jogador_atual == jogador1 else (jogador1, "X")

if __name__ == "__main__":
    jogo_da_velha()