
# 11. Biblioteca pandas
# A biblioteca pandas é uma das mais poderosas e amplamente usadas para manipulação e análise de dados em Python. Ela oferece estruturas de dados como DataFrames (tabelas) e Series (colunas), otimizadas para trabalhar com dados tabulares.
#  * Não é uma biblioteca nativa.
#  * Para instalar, use: pip install pandas
#  * O nome comumente atribuído ao pandas é pd.
# <!-- end list -->
import pandas as pd

# pd.DataFrame()
# Cria um DataFrame a partir de um dicionário, lista de listas, etc.
dados = {
    'Nome': ['Alice', 'Bob', 'Carlos', 'Diana'],
    'Idade': [25, 30, 35, 28],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'São Paulo']
}
df = pd.DataFrame(dados)
print("DataFrame Criado:")
print(df)
print("\n---")

# pd.read_csv('arquivo.csv')
# Serve para ler dados de um arquivo CSV e atribuí-los a um DataFrame.
# Certifique-se de ter um arquivo 'exemplo.csv' na mesma pasta ou forneça o caminho completo.
# Exemplo de conteúdo para 'exemplo.csv':
# Nome,Idade,Cidade
# Fernanda,22,Curitiba
# Gustavo,40,Porto Alegre
try:
    df_csv = pd.read_csv('exemplo.csv')
    print("DataFrame lido de 'exemplo.csv':")
    print(df_csv)
    print("\n---")
except FileNotFoundError:
    print("Arquivo 'exemplo.csv' não encontrado. Crie um para testar pd.read_csv().")
    print("Exemplo de conteúdo para 'exemplo.csv':\nNome,Idade,Cidade\nFernanda,22,Curitiba\nGustavo,40,Porto Alegre\n---")


# df.head(n)
# Exibe as primeiras 'n' linhas do DataFrame (padrão é 5).
print("Primeiras 2 linhas do DataFrame:")
print(df.head(2))
print("\n---")

# df.info()
# Fornece um resumo conciso do DataFrame, incluindo tipos de dados e valores não nulos.
print("Informações do DataFrame:")
df.info()
print("\n---")

# df.describe()
# Gera estatísticas descritivas das colunas numéricas (contagem, média, desvio padrão, etc.).
print("Estatísticas descritivas do DataFrame:")
print(df.describe())
print("\n---")

# Seleção de colunas
print("Coluna 'Nome':")
print(df['Nome'])
print("\n---")

# Filtragem de linhas
print("Pessoas com mais de 30 anos:")
print(df[df['Idade'] > 30])
print("\n---")

# df.to_csv('nome_arquivo.csv', index=False)
# Salva o DataFrame em um arquivo CSV. index=False evita salvar o índice como uma coluna.
df.to_csv('meus_dados_salvos.csv', index=False)
print("DataFrame salvo em 'meus_dados_salvos.csv'")

######################################################

# link com mais informações
#  * pandas:
#    https://pandas.pydata.org/docs/