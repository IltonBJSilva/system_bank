from Models.database import db
from Models.conta import Conta, Transacao
from decimal import Decimal # Importe Decimal

def realizar_deposito(conta_id, valor):
    conta = Conta.query.get(conta_id)
    if not conta:
        return False, "Conta não encontrada."

    # Converta o valor para Decimal
    valor_decimal = Decimal(str(valor)) # Converte float para string e depois para Decimal

    if valor_decimal <= 0:
        return False, "O valor do depósito deve ser positivo."

    conta.saldo += valor_decimal # Use o valor_decimal
    transacao = Transacao(conta_id=conta.id, tipo='deposito', valor=valor_decimal) # Use o valor_decimal
    db.session.add(transacao)
    db.session.commit()
    print(f'Valor R$:{valor_decimal:.2f} Depositado com sucesso na conta {conta.id}')
    return True, "Depósito realizado com sucesso!"