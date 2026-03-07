

# 3. Biblioteca os
# A biblioteca os (Operating System) fornece uma maneira de interagir com o sistema operacional. É usada para manipulação de arquivos e diretórios, variáveis de ambiente e outras operações do sistema.
#  * É uma biblioteca nativa do Python.
#  * Não precisa de instalação.
#  * Não possui um nome comumente atribuído na importação, geralmente importada como import os.
# <!-- end list -->
import os

# os.getcwd()
# Retorna o diretório de trabalho atual.
print(f"Diretório de trabalho atual: {os.getcwd()}")

# os.listdir(caminho)
# Lista o conteúdo de um diretório.
# Cuidado: Para usar em um diretório específico, o caminho deve existir.
# Exemplo: print(os.listdir('/caminho/para/seu/diretorio'))
print(f"Conteúdo do diretório atual: {os.listdir('.' or os.getcwd())}")

# os.mkdir(nome_diretorio)
# Cria um novo diretório.
# Cuidado: Se o diretório já existir, gerará um erro. Use os.makedirs() para criar diretórios aninhados.
if not os.path.exists("novo_diretorio"):
    os.mkdir("novo_diretorio")
    print("Diretório 'novo_diretorio' criado.")
else:
    print("Diretório 'novo_diretorio' já existe.")

# os.path.exists(caminho)
# Verifica se um arquivo ou diretório existe.
print(f"O arquivo 'meu_arquivo.txt' existe? {os.path.exists('meu_arquivo.txt')}")

# os.remove(caminho_arquivo)
# Remove um arquivo.
# Cuidado: Apenas use se tiver certeza que quer apagar o arquivo.
# if os.path.exists("arquivo_para_remover.txt"):
#     os.remove("arquivo_para_remover.txt")
#     print("Arquivo 'arquivo_para_remover.txt' removido.")

# os.rmdir(caminho_diretorio)
# Remove um diretório vazio.
# Cuidado: Apenas use se tiver certeza que quer apagar o diretório.
# if os.path.exists("diretorio_vazio"):
#     os.rmdir("diretorio_vazio")
#     print("Diretório 'diretorio_vazio' removido.")

######################################################

# # link com mais informações
#  * os (Python Standard Library):
#    https://docs.python.org/3/library/os.html

