#Cadastro
from flask import Flask,request, render_template

app = Flask (__name__)

@app.route('/cadastro', methods=['GET'])
def cadastro():
    return render_template("cadastro.html")

@app.route('/processar_cadastro', methods=['GET'])
def processarCadastro():
    cpf = request.form.get('cpf')
    nome = request.form.get('nome')
    sobrenome = request.form.get('sobrenome')
    sexo = request.form.get('sexo')
    senha = request.form.get('senha')
    print(cpf,nome,sobrenome,sexo,senha)
    return render_template("cadastro.html")

if __name__  == '__main__' :
    app.run(host='0.0.0.0', port=5000)
    
   
