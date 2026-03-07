# -*- coding: utf-8 -*-
"""
Este arquivo contém exemplos de código para o projeto "Sistema de Gerenciamento de Biblioteca Pessoal",
demonstrando como conectar Python ao MySQL, definir a classe Livro e implementar
as operações CRUD (Create, Read, Update, Delete).
"""

# pip install pymysql
import mysql.connector
import pymysql
conexao = pymysql.connect(user='root',password='InfoLabin012025', host= 'localhost', database= 'biblioteca')


# import mysql.connector # importação completa do módulo mysql.connector
# from mysql.connector import errorcode # Importa o módulo de erros para tratar exceções específicas do MySQL

# # --- Configuração da Conexão com o Banco de Dados ---
# # Substitua pelos detalhes do seu servidor MySQL

# # --- Função para Conectar ao Banco de Dados ---


# def conectar_bd():
#     """Estabelece a conexão com o banco de dados MySQL."""
#     try:
#         # conn = mysql.connector.connect(**DB_CONFIG)
#         conn = pymysql.connect(DB_CONFIG)
#         print("Conexão com o banco de dados estabelecida com sucesso!")
#         return conn
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             print("Erro: Nome de usuário ou senha do MySQL inválidos.")
#         elif err.errno == errorcode.ER_BAD_DB_ERROR:
#             print(f"Erro: O banco de dados '{DB_CONFIG['database']}' não existe.")
#             # Opcional: Tentar criar o banco de dados se ele não existir
#             # criar_banco_de_dados()
#             # return conectar_bd() # Tentar conectar novamente
#         else:
#             print(f"Erro ao conectar ao MySQL: {err}")
#         return None

# conexao = conectar_bd()



# # --- Opcional: Função para Criar o Banco de Dados e a Tabela (se não existirem) ---
# def configurar_banco():
#     """Cria o banco de dados e a tabela 'livros' se não existirem."""
#     try:
#         # Conecta sem especificar o banco de dados inicialmente
#         temp_config = DB_CONFIG.copy()
#         del temp_config['database']
#         conn = mysql.connector.connect(**temp_config)
#         cursor = conn.cursor()

#         # Cria o banco de dados
#         try:
#             cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']} DEFAULT CHARACTER SET 'utf8'")
#             print(f"Banco de dados '{DB_CONFIG['database']}' verificado/criado.")
#         except mysql.connector.Error as err:
#             print(f"Falha ao criar banco de dados: {err}")
#             return

#         # Usa o banco de dados recém-criado/verificado
#         conn.database = DB_CONFIG['database']

#         # Cria a tabela livros
#         tabela_livros_sql = """
#         CREATE TABLE IF NOT EXISTS livros (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             titulo VARCHAR(255) NOT NULL,
#             autor VARCHAR(255) NOT NULL,
#             ano_publicacao INT,
#             isbn VARCHAR(20) UNIQUE
#         )
#         """
#         try:
#             cursor.execute(tabela_livros_sql)
#             print("Tabela 'livros' verificada/criada com sucesso.")
#         except mysql.connector.Error as err:
#             print(f"Falha ao criar tabela 'livros': {err}")

#         cursor.close()
#         conn.close()

#     except mysql.connector.Error as err:
#         print(f"Erro geral de configuração do banco: {err}")

# # --- Classe Livro ---
# class Livro:
#     """Representa um livro na biblioteca pessoal."""
#     def __init__(self, titulo, autor, ano_publicacao, isbn, id=None):
#         """Construtor da classe Livro."""
#         self.id = id  # ID será None ao criar um novo livro, preenchido após salvar no BD
#         self.titulo = titulo
#         self.autor = autor
#         self.ano_publicacao = ano_publicacao
#         self.isbn = isbn

#     def __str__(self):
#         """Retorna uma representação em string do objeto Livro."""
#         return f"ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}, ISBN: {self.isbn}"

#     # --- Métodos CRUD associados à classe Livro ---

#     def salvar(self, conn):
#         """Salva (insere) o livro no banco de dados."""
#         if self.id is not None:
#             print("Erro: Este livro já parece existir no banco (possui ID). Use o método atualizar().")
#             return False

#         cursor = conn.cursor()
#         sql = "INSERT INTO livros (titulo, autor, ano_publicacao, isbn) VALUES (%s, %s, %s, %s)"
#         valores = (self.titulo, self.autor, self.ano_publicacao, self.isbn)

#         try:
#             cursor.execute(sql, valores)
#             conn.commit()  # Efetiva a transação
#             self.id = cursor.lastrowid # Recupera o ID gerado pelo banco
#             print(f"Livro '{self.titulo}' salvo com sucesso! ID: {self.id}")
#             return True
#         except mysql.connector.Error as err:
#             print(f"Erro ao salvar livro: {err}")
#             conn.rollback() # Desfaz a transação em caso de erro
#             return False
#         finally:
#             cursor.close()

#     def atualizar(self, conn):
#         """Atualiza os dados do livro no banco de dados."""
#         if self.id is None:
#             print("Erro: Este livro não possui ID, não pode ser atualizado. Salve-o primeiro.")
#             return False

#         cursor = conn.cursor()
#         sql = "UPDATE livros SET titulo = %s, autor = %s, ano_publicacao = %s, isbn = %s WHERE id = %s"
#         valores = (self.titulo, self.autor, self.ano_publicacao, self.isbn, self.id)

#         try:
#             cursor.execute(sql, valores)
#             conn.commit()
#             if cursor.rowcount > 0:
#                 print(f"Livro ID {self.id} ('{self.titulo}') atualizado com sucesso!")
#                 return True
#             else:
#                 print(f"Nenhum livro encontrado com ID {self.id} para atualizar.")
#                 return False
#         except mysql.connector.Error as err:
#             print(f"Erro ao atualizar livro ID {self.id}: {err}")
#             conn.rollback()
#             return False
#         finally:
#             cursor.close()

#     def excluir(self, conn):
#         """Exclui o livro do banco de dados."""
#         if self.id is None:
#             print("Erro: Este livro não possui ID, não pode ser excluído.")
#             return False

#         cursor = conn.cursor()
#         sql = "DELETE FROM livros WHERE id = %s"
#         try:
#             cursor.execute(sql, (self.id,))
#             conn.commit()
#             if cursor.rowcount > 0:
#                 print(f"Livro ID {self.id} ('{self.titulo}') excluído com sucesso!")
#                 # Resetar o ID do objeto após exclusão
#                 self.id = None
#                 return True
#             else:
#                 print(f"Nenhum livro encontrado com ID {self.id} para excluir.")
#                 return False
#         except mysql.connector.Error as err:
#             print(f"Erro ao excluir livro ID {self.id}: {err}")
#             conn.rollback()
#             return False
#         finally:
#             cursor.close()

#     # --- Métodos Estáticos/de Classe para buscar livros (não precisam de uma instância) ---
#     @staticmethod
#     def listar_todos(conn):
#         """Busca todos os livros no banco de dados e retorna uma lista de objetos Livro."""
#         livros = []
#         cursor = conn.cursor(dictionary=True) # Retorna resultados como dicionários
#         sql = "SELECT * FROM livros ORDER BY titulo"
#         try:
#             cursor.execute(sql)
#             resultados = cursor.fetchall()
#             for linha in resultados:
#                 livro = Livro(linha['titulo'], linha['autor'], linha['ano_publicacao'], linha['isbn'], linha['id'])
#                 livros.append(livro)
#             print(f"Total de {len(livros)} livros encontrados.")
#             return livros
#         except mysql.connector.Error as err:
#             print(f"Erro ao listar livros: {err}")
#             return []
#         finally:
#             cursor.close()

#     @staticmethod
#     def buscar_por_id(conn, id_livro):
#         """Busca um livro pelo seu ID e retorna um objeto Livro ou None."""
#         cursor = conn.cursor(dictionary=True)
#         sql = "SELECT * FROM livros WHERE id = %s"
#         try:
#             cursor.execute(sql, (id_livro,))
#             resultado = cursor.fetchone()
#             if resultado:
#                 livro = Livro(resultado['titulo'], resultado['autor'], resultado['ano_publicacao'], resultado['isbn'], resultado['id'])
#                 print(f"Livro encontrado: {livro}")
#                 return livro
#             else:
#                 print(f"Nenhum livro encontrado com ID {id_livro}.")
#                 return None
#         except mysql.connector.Error as err:
#             print(f"Erro ao buscar livro por ID {id_livro}: {err}")
#             return None
#         finally:
#             cursor.close()

# # --- Função Principal para Demonstração ---
# if __name__ == "__main__":
#     print("--- Sistema de Gerenciamento de Biblioteca Pessoal ---")

#     # 1. Configurar o banco (criar DB e tabela se necessário)
#     #    Execute isso uma vez ou quando precisar garantir que a estrutura existe.
#     #    Lembre-se de ajustar a senha em DB_CONFIG!
#     # configurar_banco()
#     # input("Banco configurado (se necessário). Pressione Enter para continuar...")

#     # 2. Conectar ao banco de dados
#     conexao = conectar_bd()

#     if conexao and conexao.is_connected():
#         try:
#             # 3. Criar e Salvar um novo livro (Create)
#             print("\n--- Criando e Salvando Livros ---")
#             livro_novo1 = Livro("A Revolução dos Bichos", "George Orwell", 1945, "978-8535909555")
#             livro_novo1.salvar(conexao)

#             livro_novo2 = Livro("1984", "George Orwell", 1949, "978-0451524935")
#             livro_novo2.salvar(conexao)

#             livro_novo3 = Livro("O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", 1954, "978-0547928210")
#             livro_novo3.salvar(conexao)

#             # 4. Listar todos os livros (Read)
#             print("\n--- Listando Todos os Livros ---")
#             todos_os_livros = Livro.listar_todos(conexao)
#             for livro in todos_os_livros:
#                 print(livro)

#             # 5. Buscar um livro por ID (Read)
#             print("\n--- Buscando Livro por ID (Ex: ID 1) ---")
#             id_para_buscar = 1 # Use um ID que exista no seu banco
#             livro_encontrado = Livro.buscar_por_id(conexao, id_para_buscar)
#             # if livro_encontrado:
#             #     print(f"Encontrado: {livro_encontrado}")

#             # 6. Atualizar um livro (Update)
#             print("\n--- Atualizando um Livro (Ex: ID 1) ---")
#             if livro_encontrado: # Reutiliza o livro encontrado anteriormente
#                 livro_encontrado.ano_publicacao = 1946 # Altera o ano
#                 livro_encontrado.titulo = "A Revolução dos Bichos (Edição Revisada)" # Altera o título
#                 livro_encontrado.atualizar(conexao)

#                 # Verificar a atualização buscando novamente
#                 print("\n--- Verificando Atualização (Buscando ID 1 novamente) ---")
#                 Livro.buscar_por_id(conexao, id_para_buscar)
#             else:
#                 print(f"Não foi possível atualizar, livro com ID {id_para_buscar} não encontrado inicialmente.")

#             # 7. Excluir um livro (Delete)
#             print("\n--- Excluindo um Livro (Ex: ID 2) ---")
#             id_para_excluir = 2 # Use um ID que exista
#             livro_para_excluir = Livro.buscar_por_id(conexao, id_para_excluir)
#             if livro_para_excluir:
#                 livro_para_excluir.excluir(conexao)
#             else:
#                 print(f"Não foi possível excluir, livro com ID {id_para_excluir} não encontrado.")

#             # 8. Listar todos os livros novamente para ver o resultado
#             print("\n--- Listando Todos os Livros Após Exclusão ---")
#             Livro.listar_todos(conexao)

#         except Exception as e:
#             print(f"Ocorreu um erro inesperado durante a execução: {e}")

#         finally:
#             # 9. Fechar a conexão
#             if conexao and conexao.is_connected():
#                 conexao.close()
#                 print("\nConexão com o banco de dados fechada.")
#     else:
#         print("Não foi possível conectar ao banco de dados. Verifique as configurações e o status do servidor MySQL.")

#     print("\n--- Fim da Demonstração ---")
