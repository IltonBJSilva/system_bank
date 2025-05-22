from flask import Flask, render_template, request
from services.deposito import realizar_deposito
from services.saque import realizar_saque

app = Flask(__name__)

# Simula uma conta fixa (só pra testes)
conta = {
    'saldo': 0.0,
    'extrato': [],
    "saques_diarios": 0
}

@app.route('/home')
def home():
    nome = "Ilton Batista"
    return render_template('index.html', nome=nome, conta=conta)

@app.route('/deposito', methods=['POST'])
def deposito():
    valor = request.form.get('valor', type=float)
    conta['valor'] = valor
    realizar_deposito(conta, valor)
    return render_template('index.html', conta=conta, sucesso_deposito=True)


@app.route('/saque', methods=['POST'])
def saque():
    saque = request.form.get('saque', type=float)
    realizar_saque(conta, saque)
    return render_template('index.html', conta=conta, sucesso_saque=True)



if __name__ == '__main__':
    app.run(debug=True)
