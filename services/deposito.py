

def realizar_deposito(conta, valor):
    conta["saldo"] += valor
    conta["extrato"].append(f"Depósito: R$ {valor}")


    print(f'Valor R$:{valor} Depositado com sucesso')
    return conta