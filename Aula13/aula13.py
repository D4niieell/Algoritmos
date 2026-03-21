import pymysql as pySQL
print(pySQL.version_info)

# CONEXÃO COM O BANCO DE DADOS
conexao = pySQL.connect(
    host="localhost",              # endereco do servidor (local = "localhost") 
    user="root",                   # usuario do MySQL   
    password="",                   # senha do MySQL
    database="bd_livrariaonline",  # banco que você já criou
    port=3306                      # porta padrão do MySQL (opcional) 
)

# Cria o cursor - versão simples (retorna {"coluna": valor})
cursor = conexao.cursor(pySQL.cursors.DictCursor)

# | Buscar todos os registros |
cursor.execute("SELECT * FROM clientes")
todos = cursor.fetchall()

# for cliente in todos:
#     print(cliente["nome"], cliente["email"], "-", cliente["telefone"])

# | Buscar um unico registro por ID |
# cursor.execute("SELECT nome, id_cliente FROM clientea WHERE id_cliente = 1")
# cliente = cursor.fetchone()
# print(cliente) # {'id': 1, nome, 'Maria', 'email': '...'}

# | Buscar com filtro dainâmico (SEGURO) |
nome_busca = "Ursula%"
cursor.execute("SELECT * FROM clientes WHERE nome LIKE %s", (nome_busca),)

resultado = cursor.fetchall()
print(resultado)