def realizar_saque(conta, valor):
    conta["saldo"] -= valor
    conta["saques_diarios"] += 1

    conta["extrato"].append(f"Saque: R$ {valor:.2f}")
    conta["extrato"].append(f"Saque Diário nº: {conta['saques_diarios']}")

    print(f'Valor R$:{valor:.2f} sacado com sucesso')
    return conta
