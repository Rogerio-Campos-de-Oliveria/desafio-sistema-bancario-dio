largura = 30  
print("-=" * (largura // 2))
print("BANCO DIO".center(largura))
print("-=" * (largura // 2))

print("\nSeja bem-vindo ao Banco DIO!")
nome = input("\nPor favor, informe o seu nome: ")
print(f"\nOlá, {nome}! Seja bem-vindo ao Banco DIO!")
print("Por favor, selecione a operação desejada:")

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("- Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação Negada! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("- Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nOperação Negada! Saldo Insuficiente.")

        elif excedeu_limite:
            print("\nSaque Não Realizado! O valor do saque excede o limite(R$ 500,00).")

        elif excedeu_saques:
            print("\nOperação Não Permitida! Número máximo de saques excedido.(3 saques)")

        elif valor > 0:
            saldo -= valor
            extrato += f"\nSaque Realizado: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("\nOperação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print(f"\nCódigo {opcao} inválida! Por favor selecione novamente a opção desejada.")