import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Inicializa a variável de contagem de tentativas
tentativas = 0

print("Bem-vindo ao jogo Quente e Frio!")
print("Tente adivinhar o número secreto entre 1 e 100.")

while True:
    # Solicita um palpite ao jogador
    palpite = int(input("Digite o seu palpite: "))
    
    # Incrementa o contador de tentativas
    tentativas += 1
    
    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número secreto ({numero_secreto}) em {tentativas} tentativas.")
        break
    else:
        # Calcula a diferença entre o palpite e o número secreto
        diferenca = abs(numero_secreto - palpite)
        
        # Dá dicas "quente" ou "frio" com base na diferença
        if diferenca <= 10:
            print("Quente!")
        else:
            print("Frio!")
