import pandas as pd

nome = str(input("Digite o seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

#Criacao de um dicionario para receber os dados digitados pelo usuario
dados = {
    "nome": [nome],
    "idade": [idade],
    "altura": [altura]
}

# DataFrame é a criacao de um excel no formato que o pandas entende para trbalhar com os dados
excel = pd.DataFrame(dados)

# to_excel() > serve criar uma nova planilha, pegar os dados digitados pelo usuario em formato DataFrame e gravar os dados na planilha criada

excel.to_excel("Aula12\cadastro_alunos.xlsx", index=False)

# LOC > NUMERO
# Ler o excel
leitura_excel = pd.read_excel("Aula12\cadastro_alunos.xlsx")
nova_linha = len(leitura_excel)

leitura_excel.loc[nova_linha, "nome"] = dados["nome"]
leitura_excel.loc[nova_linha, "idade"] = dados["idade"]
leitura_excel.loc[nova_linha, "altura"] = dados["altura"]

print(leitura_excel["nome"])

# APAGAR LINHAS DE UMA PLANILHA
leitura_excel = leitura_excel.drop(5)

leitura_excel.loc[2, "nome"] = dados["nome"]
leitura_excel.loc[2, "idade"] = dados["idade"]
leitura_excel.loc[2, "altura"] = dados["altura"]


# SALVAR
leitura_excel.to_excel("Aula12\cadastro_alunos.xlsx", index=False)