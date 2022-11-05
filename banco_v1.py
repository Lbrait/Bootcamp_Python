from time import sleep
menu = """

[ 1 ] Depositar
[ 2 ] Sacar
[ 3 ] Extrato
[ 0 ] Sair

--> """ 

saldo = 0
limite = 500
saques = 0
extrato = ""
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor de depósito: "))
        sleep(1)

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"   
            print(f"\nDepósito de R${valor:.2f} concluído!")  
        
        else: 
            print("Falha na operação! O valor informado é inválido.")
    
    elif opcao == "2":
        valor = float(input("Digite o valor de saque: "))
        print("Consultando aprovação do saque...\n")

        sleep(1)

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na operação! Você não tem saldo suficiente para o valor de saque informado.")
        
        elif excedeu_limite:
            print("Falha na operação! O valor informado excede o limite de saque.")
        
        elif excedeu_saques:
            print("Falha na operação! Você atingiu o limite de saques.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            saques += 1
            print(f"Saque de R${valor:.2f} concluído!")
        
        else:
            print("Falha na operação! Informe um valor válido.")

    elif opcao == "3":
        print("Consutando seu extrato...\n")
        sleep(1)
        print("Extrato Bancário:\n")
        print("Sem movimentações realizadas" if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")
    
    elif opcao == "0":
        print("Finalizando...")
        sleep(1)
        print("Volte sempre! :)")
        break
    
    else:
        print("\nDigite uma opção válida!")
        continue