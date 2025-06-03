from flask import Flask, render_template, request, redirect, url_for, flash
from services.deposito import realizar_deposito
from services.saque import realizar_saque
from Models.database import db, init_db
from Models.conta import Conta, Transacao
from datetime import datetime
from sqlalchemy.orm import joinedload # Importe o joinedload

app = Flask(__name__)
app.secret_key = 'supersecretkey' # Necessário para usar flash messages
init_db(app)

# Simula uma conta fixa (só pra testes) - Agora buscaremos do DB
# Para fins de teste, você pode criar uma conta inicial no banco de dados.
# Por exemplo, execute isso uma vez para criar a primeira conta:
# with app.app_context():
#     if not Conta.query.first():
#         nova_conta = Conta(saldo=0.0, saques_diarios=0)
#         db.session.add(nova_conta)
#         db.session.commit()

@app.route('/')
@app.route('/home')
def home():
    nome = "Ilton Batista"
    # Pega a primeira conta para demonstração, carregando as transações EAGERLY
    conta_db = Conta.query.options(joinedload(Conta.transacoes)).first() # <-- MUDANÇA AQUI!

    if not conta_db:
        flash("Nenhuma conta encontrada. Criando uma conta de demonstração.", "info")
        with app.app_context():
            nova_conta = Conta(saldo=0.0, saques_diarios=0)
            db.session.add(nova_conta)
            db.session.commit()
            conta_db = nova_conta # Você precisará refazer a query com eager loading se a conta for nova aqui

            # Se a conta acabou de ser criada, carregue-a com as transações (mesmo que vazias)
            # para evitar o erro se ela for usada imediatamente.
            conta_db = Conta.query.options(joinedload(Conta.transacoes)).filter_by(id=nova_conta.id).first()


    # Para exibir o extrato na tela, precisamos formatar os itens.
    extrato_formatado = []
    # Ordene as transações por data para um extrato mais organizado
    for transacao in sorted(conta_db.transacoes, key=lambda t: t.data): # Adicionei sort
        if transacao.tipo == 'deposito':
            extrato_formatado.append(f"Depósito: R$ {transacao.valor:.2f} em {transacao.data.strftime('%d/%m/%Y %H:%M:%S')}")
        elif transacao.tipo == 'saque':
            extrato_formatado.append(f"Saque: R$ {transacao.valor:.2f} em {transacao.data.strftime('%d/%m/%Y %H:%M:%S')}")

    # Adicionar o contador de saques diários ao extrato, ou talvez exibi-lo separadamente no HTML
    extrato_formatado.append(f"Saques Diários: {conta_db.saques_diarios}")


    return render_template('index.html', nome=nome, conta=conta_db, extrato_formatado=extrato_formatado)


@app.route('/deposito', methods=['POST'])
def deposito():
    valor = request.form.get('valor', type=float)
    conta_id = Conta.query.first().id # Pega o ID da primeira conta para demonstração
    sucesso, mensagem = realizar_deposito(conta_id, valor)
    if sucesso:
        flash(mensagem, "success")
    else:
        flash(mensagem, "error")
    return redirect(url_for('home'))


@app.route('/saque', methods=['POST'])
def saque():
    valor_saque = request.form.get('saque', type=float)
    conta_id = Conta.query.first().id # Pega o ID da primeira conta para demonstração
    sucesso, mensagem = realizar_saque(conta_id, valor_saque)
    if sucesso:
        flash(mensagem, "success")
    else:
        flash(mensagem, "error")
    return redirect(url_for('home'))

# Rota para download do extrato (opcional, mas bom para portfolio)
@app.route('/download_extrato')
def download_extrato():
    conta_db = Conta.query.first()
    if not conta_db:
        flash("Nenhuma conta para gerar extrato.", "error")
        return redirect(url_for('home'))

    filename = f"extrato_conta_{conta_db.id}_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write(f"Extrato da Conta: {conta_db.id}\n")
        f.write(f"Saldo Atual: R$ {conta_db.saldo:.2f}\n")
        f.write("\nTransações:\n")
        for transacao in conta_db.transacoes:
            f.write(f"{transacao.tipo.capitalize()}: R$ {transacao.valor:.2f} em {transacao.data.strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write(f"Saques Diários Realizados: {conta_db.saques_diarios}\n")

    flash(f"Extrato salvo em '{filename}'", "success")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)