# 13. Biblioteca shutil
# A biblioteca shutil (do inglês "shell utilities") fornece operações de alto nível em arquivos e coleções de arquivos. É muito útil para copiar, mover, renomear e excluir arquivos e diretórios de forma mais robusta e simples do que com a biblioteca os.
#  * É uma biblioteca nativa do Python.
#  * Não precisa de instalação.
#  * Não possui um nome comumente atribuído na importação, geralmente importada como import shutil.
# <!-- end list -->
import shutil
import os # Geralmente usada em conjunto com 'os' para verificar caminhos, etc.

# --- Preparação para os exemplos (cria alguns arquivos e pastas temporárias) ---
# Cria um diretório de teste
if not os.path.exists("pasta_origem"):
    os.mkdir("pasta_origem")
    print("Diretório 'pasta_origem' criado.")

# Cria um arquivo de texto dentro da pasta de origem
with open("pasta_origem/arquivo_exemplo.txt", "w") as f:
    f.write("Este é um arquivo de exemplo para shutil.")
print("Arquivo 'pasta_origem/arquivo_exemplo.txt' criado.")

# Cria uma subpasta dentro da pasta de origem
if not os.path.exists("pasta_origem/subpasta"):
    os.mkdir("pasta_origem/subpasta")
    print("Diretório 'pasta_origem/subpasta' criado.")

# Cria um segundo arquivo na subpasta
with open("pasta_origem/subpasta/outro_arquivo.log", "w") as f:
    f.write("Log de teste.")
print("Arquivo 'pasta_origem/subpasta/outro_arquivo.log' criado.")

# --- Exemplos de uso do shutil ---

# shutil.copy(origem, destino)
# Copia o arquivo 'origem' para o 'destino'.
# Se 'destino' for um diretório, o arquivo é copiado para dentro dele mantendo o nome.
# Se 'destino' for um nome de arquivo, o arquivo é copiado e renomeado para esse nome.
if os.path.exists("pasta_origem/arquivo_exemplo.txt"):
    shutil.copy("pasta_origem/arquivo_exemplo.txt", "copia_arquivo.txt")
    print("Copiado 'arquivo_exemplo.txt' para 'copia_arquivo.txt'.")
    shutil.copy("pasta_origem/arquivo_exemplo.txt", "pasta_origem/copia_dentro.txt")
    print("Copiado 'arquivo_exemplo.txt' para 'pasta_origem/copia_dentro.txt'.")

# shutil.copyfile(origem, destino)
# Copia o conteúdo (e permissões) do arquivo 'origem' para o arquivo 'destino'.
# 'destino' deve ser um arquivo, não um diretório.
if os.path.exists("pasta_origem/arquivo_exemplo.txt"):
    shutil.copyfile("pasta_origem/arquivo_exemplo.txt", "copia_apenas_conteudo.txt")
    print("Copiado conteúdo de 'arquivo_exemplo.txt' para 'copia_apenas_conteudo.txt'.")

# shutil.copytree(origem, destino)
# Copia um diretório inteiro (e todo o seu conteúdo) para um novo local.
# O 'destino' não deve existir.
if not os.path.exists("pasta_destino"):
    shutil.copytree("pasta_origem", "pasta_destino")
    print("Copiado 'pasta_origem' para 'pasta_destino' (incluindo subpastas e arquivos).")
else:
    print("Diretório 'pasta_destino' já existe. Não copiou com copytree.")

# shutil.move(origem, destino)
# Move um arquivo ou diretório de 'origem' para 'destino'.
# Se 'destino' for um diretório existente, o item é movido para dentro dele.
# Se 'destino' não existir, o item é movido e renomeado para 'destino'.
if os.path.exists("copia_arquivo.txt"):
    shutil.move("copia_arquivo.txt", "pasta_destino/arquivo_movido.txt")
    print("Movido 'copia_arquivo.txt' para 'pasta_destino/arquivo_movido.txt'.")

# shutil.rmtree(caminho_diretorio)
# Remove um diretório e todo o seu conteúdo (arquivos e subdiretórios).
# Cuidado: Esta operação é IRREVERSÍVEL! Use com extrema cautela.
if os.path.exists("pasta_origem"):
    # shutil.rmtree("pasta_origem")
    # print("Diretório 'pasta_origem' e seu conteúdo removidos.")
    # Comentei esta linha para evitar remoção acidental durante o teste.
    # Descomente para testar a remoção completa.
    print("Diretório 'pasta_origem' pronto para ser removido com shutil.rmtree().")

# --- Limpeza (opcional, para remover os diretórios criados pelos exemplos) ---
# if os.path.exists("pasta_destino"):
#     shutil.rmtree("pasta_destino")
#     print("Diretório 'pasta_destino' removido.")
# if os.path.exists("copia_apenas_conteudo.txt"):
#     os.remove("copia_apenas_conteudo.txt")
#     print("Arquivo 'copia_apenas_conteudo.txt' removido.")
# if os.path.exists("pasta_origem"):
#     shutil.rmtree("pasta_origem") # Certifique-se que o original também é limpo
#     print("Diretório 'pasta_origem' e seu conteúdo removidos.")


######################################################

# # link com mais informações
#  * Documentação oficial do módulo shutil
# Espero que este complemento seja útil para você!