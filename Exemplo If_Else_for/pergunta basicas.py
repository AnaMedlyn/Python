pontuacao = 0
print("Qual é a aula que acontece no senai?")
res1 = input()

if res1 =="python":
    pontuacao += 1
else:
    print("Infelizmente voce errou!")
    
resp2 = input ("Qual é o inicio da aula?")

if resp2 == "8h":
    pontuacao = pontuacao +1
    
else:
      print("Opa, voce nao acertou")
      
print("Sua pontuacao final foi: ", pontuacao)


    
    
    
