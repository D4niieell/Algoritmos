# Atividade 1 — Salvar Cadastro
# Crie um programa que:
# Peça nome e idade
# Salve no arquivo cadastros.txt
# Cada cadastro deve ficar em uma linha
# Dica de código:

nome = input("Digite o seu nome: ")
idade = input("Digite sua idade: ")
with open("cadastros.txt", "w") as 