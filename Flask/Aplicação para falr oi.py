#Aplicação para falar oi

from flask import Flask

app = Flask (__name__)

@app.route('/')
def ola():
    return "Oi"

if __name__  == '__main__' :
    app.run()