# API
# Introdução a APIs em Python

import requests

URL = "https://rickandmortyapi.com/api/character"

resposta = requests.get(URL) # retorno status 200

json = resposta.json() # retornar o JSON
print(json)

personagem = json["results"] # Consulta os meus personagens

print(personagem)
# laço de repetição para consulyat apenas os nomes dos personagens
for nome_personagem in personagem:
    print(nome_personagem["name"]) 

# Retornar mais informações além do nome
for mais_info in personagem:
    print("Nome: ", mais_info["name"])
    print("Status: ", mais_info["status"])
    print("Especie: ", mais_info["species"])
    print("----------------------------------")

# Pedir ao usuario para digitar um ID e retornar da API o personagem referentea esse ID
id = int(input("Digite um numero inteiro: "))
link_API = f"https://rickandmortyapi.com/api/character/{id}"
resposta = requests.get(link_API)
novo_json = resposta.json()
print("Nome: ", novo_json["name"])
print("Status: ", novo_json["status"])
print("Especie: ", novo_json["species"])
print("----------------------------------")

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