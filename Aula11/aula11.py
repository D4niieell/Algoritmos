# Importando bibliotecas
# Para usar uma biblioteca usamos a palavra import.
import random
import math
import datetime

numero_aleatorio = random.randint(1000, 2000)

# GRANDIANT -> Gera apenas numeros aleatorios
print(numero_aleatorio)

# Sorteio de aluno
alunos = ["Israel", "Adenilson", "Anna", "Wellington", "Jonathan", "Isabelly", "JP.",
          "Luis Felipe", "Iara", "Vanessa", "Daniel", "João P.", "Lucas", "Bernardo", "Micael"
          "Camila", "Stefany", "Guilherme", "Micael", "Kauan"]

# Biblioteca random
# CHOICE -> escolher de forma aleatoria
sorteado = random.choice(alunos)
sorteado2 = random.choice(alunos)
print("Dupla Dinamica:", sorteado, " - ", sorteado2)

# Biblioteca math
# SQRT -> raiz quadrada
numero = 16
raiz = math.sqrt(numero)
print(raiz)

# Elevar um numero
print(math.pow(2, 2))

# Trabalhando com datas
agora = datetime.datetime.now()
print(agora.year)