# Abrindo Arquivos
# Em Python usamos a função open()
# "w" - Escreve (apaga tudo e escreve de novo)
# "a" - Adiciona conteúdo ao final
# "r" - Lê o arquivo
open("nota.txt", "w")

# Escrevendo em Arquivo
# Abrir um arquivo e digiar informações
# with → garante que o arquivo será fechado corretamente
# "dados.txt" → nome do arquivo
# "w" → modo de escrita
# arquivo.write() → escreve dentro do arquivo
with open("nota.text", "w") as nota_aluno:
    nota_aluno.write("Ola mundo")

# Lendo Arquivos
# "r" → modo leitura
# .read() → lê todo o conteúdo
with open("nota.txt", "r") as leitura_arquivo:
    recebe_texto = leitura_arquivo.read()
    print(recebe_texto)

# Adicionando Conteúdo sem Apagar
# "a" → append (adiciona no final)
# \n → quebra de linha
# Adicionar um texto ao final do seu arquivo
with open("nota.txt", "a") as adiciona_novo_texto:
    adiciona_novo_texto.write("\n Aqui tem uma nova linha de texto") 



