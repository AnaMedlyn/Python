#aplicação para somar 2 numeros.
from flask import Flask,request

app = Flask (__name__)

@app.route('/somar', methods=['GET'])
def somar():
    
    num1 = float (request.args.get('num1'))
    num2 = float (request.args.get('num2'))
     
    return "resultado: " + str(num1 + num2)

if __name__  == '__main__' :
    app.run()
    
    
    #http://127.0.0.1:5000/somar?num1=10&num2=40
    #colocar na barra de pesquisa do site