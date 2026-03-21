import pymysql as pySQL

# Arquivo destinado a trabalhar com banco de dados e fazer as operações UPDATE, INSERT E DELETE

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
try:
    # | INSERT: adicionar um novo registro |
    # sql_insert = "INSERT INTO clientes (nome, email) VALUES (%s, %s)"
    # cursor.execute(sql_insert, ("Ana Lima", "ana@email.com"))
    # conexao.commit() # <- confirma o INSERT
    # print("inserindo com sucesso!  ID:", cursor.lastrowid)
    # # lastrowid -> RETORNAR O ID QUE FOI CRIADO
    
    # # | UPDATE: atualizar um registro exeistente |
    # sql_update = "UPDATE clientes SET email = %s WHERE id = %s"
    # cursor.execute(sql_update, ("novo@email.com", 1))
    # conexao.commit() # <- confirma o UPDATE
    # print("Linhas afetadas:", cursor.ro)

    # | DELETE: remover um registro |
    cursor.execute("DELETE FROM clientes WHERE id = %s", (5,))
    conexao.commit() # <- confirma o DELETE

except Exception as erro:
    conexao.rollback() # <- desfaz tudo se algo deu errado
    print("Erro! Operação revertida:", erro)
finally:
    cursor.close()
    conexao.close() # <- fechar a conexão com o banco de dados