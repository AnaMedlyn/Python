# Solicita ao usuário para inserir uma palavra
palavra = input("Insira uma palavra: ")

# Inicializa a contagem de vogais
contagem_vogais = 0

# Loop for para percorrer cada caractere na palavra
for letra in palavra:
    # Verifica se a letra é uma vogal maiúscula ou minúscula
    if letra.upper() in ['A', 'E', 'I', 'O', 'U']:
        contagem_vogais += 1

# Imprime o resultado
print("O número de vogais na palavra é:", contagem_vogais)