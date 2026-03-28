# Nome do arquivo: banco_tabajara.py
# nome excel: base_BANCO_TABAJARA

# Vamos criar um sistema bancário chamado banco tabajara, nosso banco terá as seguintes caracteristicas:

"""
Contas:
- Corrente
- Poupança
- Salario

Dados do cliente que vamos guardar em um excel:
- nome_cliente
- tipo_conta
- numero_conta
- cpf
- agencia
- extrato_bancario
- deposito
- saque

Obs: Esse serão os nomes das colunas no nosso excel

Seguintes regras de saque para cada conta:
Saques na conta Corrente: 5% de taxa
Saques na conta Corrente: Poupança 0% de taxa
Saques na conta Corrente: Salario 2% de taxa

DESENVOLVIMENTO

Crie um menu com as seguintes opções:
1 - Criar conta
2 - Acessar conta

Regras para cada opção no menu

1 - Criar conta > Solicitar ao usuario para digitar as seguintes informações:
- nome_cliente
- cpf
- tipo_conta

O outros campos serão gerados de forma automatica
- numero_conta = Será gerada de forma sequencial começando do 0 até 100
- agencia = será gerado de forma sequencial começando do 400 até 700
- extrato_bancario = valor inicial terá que começar em 0

Ao finalizar mostrar para o usuário o nome_cliente, cpf, tipo_conta, numero_conta, agencia, extrato_bancario


2 - Acessar conta > É necessário que o usuário passe os seguites dados:
- cpf
- numero_conta
> Precisa percorrer o excel e encontra o cliente com os mesmo dados de cpf e numero_conta caso encontre o cliente na base retornar uma mensagem: "Bem-vindo "nome_cliente" ao banco Tabajara"
SE NÃO se o usuario não existir na base então retornamos uma mensagem "Usuário não encontrado, tentar novamente ou realizar o cadastro"
"""

"""
SEGUNDA PARTE

Quando o usuário selecionar a opção "2 - Acessar conta" e o campo cpf e numero_conta forem encontrados na base, além de mostrar a mensagem acima, mostre um menu com as seguintes opções:

1 - Saque
2 - Deposito
3 - Saldo

Regras para cada opção
1 - Saque > solicitar ao usuário que digite um valor, podendo ser inteiro ou de ponto flutuante:
- O valor solicitado para saque não pode ser maior que o valor em conta(coluna extrato_bancario), se for digitado um valor maior encerre o fluxo e mostre a mensagem "Valor maior que o disponivel em conta";
- Se o valor for menor que o disponivel em conta, realizar a subitração (do valor solicitado - o valor na coluna extrato_bancario - taxa de saque), quando a operação for realizada com sucesso mostre a mensagem 
print("================================================")
print(      Saque realizado com sucesso!)
print(      Saque: (valor Solicitado)
print(      Valor em conta: (coluna extrato_bancario))
print(      Taxa para saque: (seguir regras para cada conta))
print(      Valor de desconto saque: (seguir regras para cada conta))
print("================================================\n")

OBS: Criar a logica de desconto da taxa para cada conta especifica



2 - Deposito > solicitar ao usuário que digite um valor, podendo ser inteiro ou de ponto flutuante, se o valor for valido então somar com o valor já existente na coluna "extrato_bancario"  ao finalizar mostrar o seguinte template
print("================================================")
print("   	Valor depositado: (Variavel do valor depositado)")
print("   	Saldo em conta: (Coluna extrato_bancario)
print("================================================\n")
valor final da conta bancaria(coluna extrato_bancario);
- Se o usuário digita um número negativo então encerre o fluxo e mostre a mensagem "Numero invalido, operação encerrada";



3 - Saldo > Mostre em tela o seguinte template
print("================================================")
print("   Tipo conta: (coluna tipo_conta)")
print("   Saldo em conta: (Coluna extrato_bancario)
print("================================================\n")
"""

import pandas as pd
import os

print("Digite as seguintes informações: ")
print("1 > Criar conta ")
print("2 > Acessar conta ")
opcao = int(input("R: "))

caminho_excel = "Aula14\Base_BANCO_TABAJARA.xlsx"

if opcao == 1:
    print("Opção 1 selecionada")
    
    if os.path.exists(caminho_excel):
        df = pd.read_excel(caminho_excel)

        nome_cliente = str(input("Digite o seu nome: "))
        tipo_conta = str(input("Digite seu tipo de conta: "))
        cpf = float(input("Digite seu CPF: "))

        df["numero_conta"] = df["numero_conta"].astype(int)
        numero_conta = df["numero_conta"].max() + 1

        df["agencia"] = df["agencia"].astype(int)
        agencia = df["agencia"].max() + 1

        extrato_bancario = 0
        
        dados = {
            "nome_cliente": [nome_cliente],
            "cpf": [cpf],
            "tipo_conta": [tipo_conta],
            "numero_conta": [numero_conta],
            "agencia": [agencia],
            "extrato_bancario": [extrato_bancario]
        }

        nova_linha = len(df)

        df.loc[nova_linha, "nome_cliente"] = dados["nome_cliente"]
        df.loc[nova_linha, "cpf"] = dados["cpf"]
        df.loc[nova_linha, "tipo_conta"] = dados["tipo_conta"]
        df.loc[nova_linha, "numero_conta"] = dados["numero_conta"]
        df.loc[nova_linha, "agencia"] = dados["agencia"]
        df.loc[nova_linha, "extrato_bancario"] = dados["extrato_bancario"]

        df.to_excel("Aula14\Base_BANCO_TABAJARA.xlsx", index=False)
    else:
        numero_conta = 0
        agencia = 400
        extrato_bancario = 0
        nome_cliente = str(input("Digite o seu nome: "))
        tipo_conta = str(input("Digite seu tipo de conta: "))
        cpf = float(input("Digite seu CPF: "))

        dados = {
            "nome_cliente": [nome_cliente],
            "cpf": [cpf],
            "tipo_conta": [tipo_conta],
            "numero_conta": [numero_conta],
            "agencia": [agencia],
            "extrato_bancario": [extrato_bancario]
        }

        excel = pd.DataFrame(dados)

        excel.to_excel("Aula14\Base_BANCO_TABAJARA.xlsx", index=False)
        print("Ação finalizada...")

if opcao == 2:
    cpf_input = input("Digite o CPF: ")
    numero_conta_input = input("Digite o número da conta: ")
    
    
    usuario_encontrado = False
    df = pd.read_excel(caminho_excel)

    for index, row in df.iterrows():
        if str(row['cpf']) == cpf_input and str(row['numero_conta']) == numero_conta_input:
            print(f"Bem-vindo {row['nome_cliente']} ao banco Tabajara")
            usuario_encontrado = True
            break

    if not usuario_encontrado:
        print("Usuario não encontrado, tentar novamente ou realizar o cadastro")


    if usuario_encontrado:
        print("\n--- O que deseja fazer? ---")
        print("1 - Saque")
        print("2 - Depósito")
        print("3 - Saldo")
        opcao_conta = int(input("Digite a opção desejada: "))

        if opcao_conta == 1:
            print("Você selecionou: Saque")
        elif opcao_conta == 2:
            print("Você selecionou: Depósito")
        elif opcao_conta == 3:
            print("Você selecionou: Saldo")
        else:
            print("Opção inválida:")
    
    if not usuario_encontrado:
        print("Usuario não encontrado, tentar novamente ou realizar o cadastro")

    if opcao_conta == 1:
        valor_saque = float(input("Digite o valor para saque: "))
        saldo_atual = row['extrato_bancario']
        tipo_conta = row['tipo_conta']

        if tipo_conta == "Corrente":
            taxa_percentual = 5
        elif tipo_conta == "Poupança":
            taxa_percentual = 0
        elif tipo_conta == "Salario":
            taxa_percentual = 2
        else:
            taxa_percentual = 0

        taxa_valor = valor_saque * (taxa_percentual / 100)
        total_descontado = valor_saque + taxa_valor

        if valor_saque > saldo_atual:
            print("Valor maior que o disponivel em conta")
        else:
            novo_saldo = saldo_atual - total_descontado
        
            print("================================================")
            print(" Saque realizado com sucesso!")      
            print(f"Saque: R$ {valor_saque:.2f}")
            print(f"Valor em conta: R$ {novo_saldo:.2f}")
            print(f"Taxa para saque: {taxa_percentual}%")
            print(f"Valor de desconto saque: {taxa_valor:.2f}")
            print("================================================\n")

    elif opcao_conta == 2:
        valor_deposito = float(input("Digite o valor para o depósito: "))

        if valor_deposito < 0:
            print("Numero inválido, operção encerrada")
        else:
            saldo_atual = row['extrato_bancario']
            novo_saldo = saldo_atual + valor_deposito

            print("================================================")
            print(f"   	Valor depositado: R$ {valor_deposito:.2f}")
            print(f"   	Saldo em conta: R$ {novo_saldo:.2f}")
            print("================================================\n")

    elif opcao_conta == 3:
        saldo_atual = row['extrato_bancario']
        tipo_conta = row['tipo_conta']

        print("================================================")
        print(f"   Tipo conta: {tipo_conta}")
        print(f"   Saldo em conta: {saldo_atual:.2f}")
        print("================================================\n")

        


        
        




