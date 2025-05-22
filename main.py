from services.deposito import realizar_deposito
from services.saque import realizar_saque
from services.extrato import gerar_extrato

def main():
    conta = {
        "saldo": 0.0,
        "extrato": [],
        "saques_diarios": 0
    }

    while True:
        print("\n1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver Extrato e Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            realizar_deposito(conta)
        elif opcao == "2":
            realizar_saque(conta)
        elif opcao == "3":
            gerar_extrato(conta)
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
