from time import *
import pymysql

class Livro():
    id = 0
    def __init__(self, titulo, autor, ano_publicacao,isbn):
        self.__titulo = titulo # o __ é usado para deixar o atributo privado 
        self.__autor = autor # isso se chama encapsulamento
        self.__ano_publicacao = ano_publicacao
        self.__isbn = isbn
        Livro.id += 1
        self.__id_livro = Livro.id
        
    
    def __str__(self):
        return f"ID: {self.__id_livro}, Título: {self.__titulo}, Autor: {self.__autor}, Ano de Publicação: {self.__ano_publicacao}, ISBN: {self.__isbn}"
    
    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo 
    
    def get_autor(self):
        return self.__autor
    
    def set_autor(self, autor):
        self.__autor = autor
    
    def get_ano_publicacao(self):
        return self.__ano_publicacao
    
    def set_ano_publicacao(self, ano_publicacao):
        self.__ano_publicacao = ano_publicacao
    
    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, isbn):
        self.__isbn = isbn

class Autor():
    id_autor = 0
    def __init__(self, nome, nacionalidade):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        Autor.id_autor += 1
        self.__id_autor = Autor.id_autor
    
    def __str__(self):
        return f"Nome: {self.__nome}, Nacionalidade: {self.__nacionalidade}, ID do Autor: {self.__id_autor}"
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_nacionalidade(self):
        return self.__nacionalidade
    
    def set_nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

def conectar_bd():
    try:
        conex = pymysql.connect(user='root',password='150520', host= 'localhost', database= 'biblioteca')
        print('Conexão com o banco de dados estabelecida com sucesso!')
        return conex
    except pymysql.Error as err:
        print('erro :', err)

def executar():
    while True:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano_publicacao = input("Digite o ano de publicação do livro: ")
        isbn = input("Digite o ISBN do livro: ")

        livri1= Livro(titulo, autor, ano_publicacao, isbn)
        print(livri1.__str__())

conectar_bd()
executar()
