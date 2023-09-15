#Verificar se numero x é primo

def verificarPrimo(numero):
    
    ehPrimo = True
    
    for i in range (2, numero):
        if numero % i == 0 :
            ehPrimo = False
            
    return ehPrimo
    
for x in range (0,10):
    if verificarPrimo(x):
        print (x, "ehPrimo")
        
#ou
        
for x in range(0,100):
    
    ehPrimo = True
    
    for i in range (2,x):
        if x % i == 0 :
            ehPrimo = False
    
    if ehPrimo:
        print(x, "eh primo")