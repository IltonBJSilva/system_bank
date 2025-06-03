from Models.database import db
from Models.conta import Conta, Transacao
from decimal import Decimal # Importe Decimal

def realizar_saque(conta_id, valor): # 'valor' aqui se refere ao valor do saque
    conta = Conta.query.get(conta_id)
    if not conta:
        return False, "Conta não encontrada."

    LIMITE_SAQUES_DIARIOS = 3
    LIMITE_VALOR_SAQUE = Decimal('500.00') # Defina o limite como Decimal

    # Converta o valor para Decimal
    valor_decimal = Decimal(str(valor)) # Converte float para string e depois para Decimal

    if conta.saques_diarios >= LIMITE_SAQUES_DIARIOS:
        return False, "Limite de saques diários atingido."

    if valor_decimal <= 0:
        return False, "O valor do saque deve ser positivo."

    if valor_decimal > LIMITE_VALOR_SAQUE:
        return False, f"O valor máximo por saque é de R$ {LIMITE_VALOR_SAQUE:.2f}."

    if conta.saldo < valor_decimal: # Compare com valor_decimal
        return False, "Saldo insuficiente."

    conta.saldo -= valor_decimal # Use valor_decimal
    conta.saques_diarios += 1
    transacao = Transacao(conta_id=conta.id, tipo='saque', valor=valor_decimal) # Use valor_decimal
    db.session.add(transacao)
    db.session.commit()
    print(f'Valor R$:{valor_decimal:.2f} sacado com sucesso da conta {conta.id}')
    return True, "Saque realizado com sucesso!"