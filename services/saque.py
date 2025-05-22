def realizar_saque(conta):
    valor = float(input('Digite o valor a ser sacado: '))
    conta["saldo"] -= valor
    conta["saques_diarios"] += 1
    
    conta["extrato"].append(f"Saque: R$ {valor}")
    conta["extrato"].append(f"Saque Diario: R$ {conta["saques_diarios"]}")

    print(f'Valor R$:{valor} sacado com sucesso')
    return conta