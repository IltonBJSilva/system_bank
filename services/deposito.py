
def realizar_deposito(conta):
    valor = float(input('Digite o valor a ser depositado: '))
    conta["saldo"] += valor
    conta["extrato"].append(f"Depósito: R$ {valor}")


    print(f'Valor R$:{valor} Depositado com sucesso')
    return conta