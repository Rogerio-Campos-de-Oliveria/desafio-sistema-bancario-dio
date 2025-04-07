def depositar_dinheiro(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso !!!")
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def sacar_dinheiro(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso !!!")
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

        return saldo, extrato

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

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar_dinheiro(saldo, valor, extrato)

        

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        saldo, extrato = sacar_dinheiro(

            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,

        )


    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")