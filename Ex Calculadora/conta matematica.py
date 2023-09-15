#Calculadora

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
         return "Não é possível dividir por zero"
    else: 
      return a / b

while True:
    print("1) adicao")
    print("2) subtracao")
    print("3) multiplicacao")
    print("4) divisao")
    print("5) sair")

    entrada = int(input("Digite uma opção: "))
    
    if entrada == 1:
        a = int(input("Digite um número A: "))
        b = int(input("Digite um número B: "))
        print("Resultado:", adicao(a, b))
        
    elif entrada == 2:
        a = int(input("Digite um número A: "))
        b = int(input("Digite um número B: "))
        print("Resultado:", subtracao(a, b))
        
    elif entrada == 3:
        a = int(input("Digite um número A: "))
        b = int(input("Digite um número B: "))
        print("Resultado:", multiplicacao(a, b))
        
    elif entrada == 4:
        a = int(input("Digite um número A: "))
        b = int(input("Digite um número B: "))
        print("Resultado:", divisao(a, b))
        
    elif entrada == 5:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")