#aplicação de um numero
from flask import Flask,request

app = Flask (__name__)

@app.route('/somar', methods=['GET'])
def somar():
    
    num1 = float (request.args.get('num1'))
    return "recebido: " + str(num1)

if __name__  == '__main__' :
    app.run()
    
     #http://127.0.0.1:5000/somar?num1=10
     #colocar na barra de pesquisa do site