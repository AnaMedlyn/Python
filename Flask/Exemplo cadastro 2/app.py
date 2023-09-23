from flask import Flask, request, render_template

app = Flask(__name__)

pessoasCadastradas = []

@app.route('/cadastro', methods=['GET'])
def cadastro():
    return render_template("cadastro.html")

@app.route('/visualizar', methods=['GET'])
def visualizar():
    return render_template("visualizacao.html", pessoas = pessoasCadastradas)
    
@app.route('/processar_cadastro', methods=['POST'])
def processarCadastro():
    cpf = request.form.get('cpf')
    nome = request.form.get('nome')
    sobrenome = request.form.get('sobrenome')
    sexo = request.form.get('sexo')
    senha = request.form.get('senha')
    
    pessoa = {}
    pessoa['cpf'] = cpf
    pessoa['nome'] = nome
    pessoa['sobrenome'] = sobrenome
    pessoa['sexo'] = sexo
    pessoa['senha'] = senha
    
    pessoasCadastradas.append(pessoa)
    
    print(pessoasCadastradas)
    
    return render_template("cadastro.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)