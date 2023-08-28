from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calcular_idade():
    if request.method == "POST":
        data_nascimento = request.form["data_nascimento"]
        data_atual = request.form["data_atual"]
        idade = calcula_idade(data_nascimento, data_atual)
        return render_template("resultado.html", idade=idade)
    return render_template("formulario.html")
    
def calcula_idade(data_nascimento, data_atual):
    data_nascimento= datetime.strptime(data_nascimento, "%d-%m-%Y")
    data_atual = datetime.strptime(data_atual, "%d-%m-%Y" )
    
    idade = data_atual.year - data_nascimento.year
    if data_atual.month < data_nascimento.month or (data_atual.month == data_nascimento.month and data_atual.day < data_nascimento.day):
        idade = idade - 1
    return idade

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)