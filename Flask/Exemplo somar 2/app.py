from flask import Flask,request

app = Flask (__name__)

@app.route('/comeco', methods=['GET'])
def comeco():
    return render_template("somadora.html")

@app.route('/somar', methods=['GET'])
def somar():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    
    return "Resultado: "+ str(num1+num2)

if __name__  == '__main__' :
    app.run(host='0.0.0.0', port=5000)
    
   