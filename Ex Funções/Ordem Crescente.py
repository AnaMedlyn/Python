#faça uma função que receba 3 valores inteiros por parâmetro e retorna-os ordenados
#em ordem crescente

def ordenarCrescente(a, b, c):
    if a > b and a > c:
        print("A é maior que B e C")
    elif b > a and b > c:
        print("B é maior que A e C")
    elif c > a and c > b:
        print("C é maior que A e B")
    else:
        print("Os valores são iguais ou ocorreu um erro na comparação")

# Exemplo de uso
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

ordenarCrescente(valor1, valor2, valor3)