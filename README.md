# Sistema Bancario

Este repositório contém uma implementação simples de um sistema bancário em Python. Desenvolvido para fins educacionais, oferece funcionalidades básicas como criação de contas, depósitos, saques e consultas de saldo. Ideal para aprender conceitos de programação orientada a objetos e manipulação de dados em Python.

Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações:

1. Depósito.
2. Saque.
3. Extrato.

Ao final, quando escolher a opção de extrato, sera salvo um arquivo file com nome que o usuario escolher e ficara salvo todas as transações e ações realizadas

## Como funciona

### Operação de Depósito

Deve ser possível depositar valores positivos para a minha conta bancaria, a v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancaria. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de Saque

O sistema deve permitir realziar 3 saques diário com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possivel sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de Extrato

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.

Os valores devem ser exibidos utilizando o formatado R$ xxx:xx, Exemplo: 1500.45 = R$ 1500.45

## Contribuição

Sinta-se livre para contribuir com este projeto e adicionar novos recursos ao gerador de senhas.
