#lista = []
#tupla = ()
#dicionario = {}

cadastroDePessoa = {}

nome = input("digite o seu nome: ")
cadastroDePessoa["nome"] = nome

print(cadastroDePessoa)

nomeAtualizado = input("atualize seu nome: ")
cadastroDePessoa["nome"] = nomeAtualizado

print(cadastroDePessoa)

if cadastroDePessoa["nome"] == "ana":
    print("é aluna")
