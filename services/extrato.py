from utils.formatador import formatar_valor

def gerar_extrato(conta):
    valor = conta["saldo"]
    valor_formatado = formatar_valor(valor)
    extrato = conta["extrato"]
    return extrato, valor_formatado