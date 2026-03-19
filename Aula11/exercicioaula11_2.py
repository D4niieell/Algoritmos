# Data da entrega: 15/03/2025

# Criar um menu para selecao
# 1 - Consultar por ID
# 2 - Consultar por nome
# 3 - Lista de personagens

# se for opcao 1:
"""
    Pedir ao usuario para digitar um ID(Numero inteiro) e retornar de dentro da API o personagem referente ao ID digitado
    Retorne todas as informações sobre o personagem
"""

# Se selecionar a opcao 2:
"""
    Pedir ao usuario para digitar nome e retornar o resultado

    OBS de codigo: para percorrer o json e retornar o nome digitado.
"""
    # for personagem in dados["results"]:
    #     print(personagem["name"])



# Se selecionar a opcao 3:
# Retornar todos os personagens
# Lista das informações que deverão ser retornadas:
"""
"results": [
"id":
"name":
"status":
"species":
"gender":
]
"origin": {
    "name": "Earth (C-137)",
},
"location": {
    "name": "Citadel of Ricks",
},
"image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg",
"""

import requests
URL = "https://rickandmortyapi.com/api/character/8"

# Solicitar que o usuario digite um numero de 1 a 3
numero_usuario = int(input("Digite um numero de 1 a 3: "))

# Verificar qual o valor que o usuario digitou e mostrar uma mensagem
# 1 - Consultar por ID
# 2 - Consultar por nome
# 3 - Lista de personagens

if numero_usuario == 1:
    print("1")

elif numero_usuario == 2:
    print("2")

# resposta = requests.get(URL)
# json = resposta.json()
# print(json)
# personagem = json["results"]
# print(personagem)
# for nome_personagem in personagem:
#     print(nome_personagem["name"])
# for mais_info in personagem:
#     print("Nome: ", mais_info["name"])
#     print("ID: ", mais_info["ID"])
#     print("Lista de personagens: ", mais_info["Lista de personagens"])
#     print("---------------------------------------")