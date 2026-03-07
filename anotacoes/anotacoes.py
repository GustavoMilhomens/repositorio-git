# my_tuple = (0, 1, 2, 3, 4, 5, 6)

# foo = list(filter(lambda x: x-0 and x-1, my_tuple))  
# print(foo)

# import pygame

# run = True
# width = 400
# height = 100
# pygame.init()
# screen = pygame.display.set_mode((width, height))
# font = pygame.font.SysFont(None, 48)
# text = font.render("Welcome to pygame", True, (255, 255, 255))
# screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
# pygame.display.flip()
# while run:
#   for event in pygame.event.get():
#    if event.type == pygame.QUIT\
#    or event.type == pygame.MOUSEBUTTONUP\
#    or event.type == pygame.KEYUP:
#     run = False



#============================================#

# from tkinter import*

# def funcao():
# 	texto1['text'] = 'ola'


# calculadora = Tk()
# calculadora.geometry('689x1200')
# calculadora.title('Calculadora')
# calculadora.config(bg='blue')

# texto=Label(calculadora,text='texto')
# texto.grid(column=0,row=0)

# botao=Button(calculadora,text='1',command=funcao)
# botao.place(x=100,y=100 )

# texto1=Label(calculadora, text='')
# texto1.place(x=290,y=290)

# calculadora.mainloop()

#============================================#


# import random , time

# while True:

#     print(random.randrange(0,30,5))
#     time.sleep(1)

# import time
# for i in range(3):
#     print('.  ', end='\r')
#     time.sleep(0.5)
#     print('.. ', end='\r')
#     time.sleep(0.5)
#     print('...', end='\r')
#     time.sleep(0.5)

#============================================#


# print(hasattr(A,'A'))
# print(hasattr(1,"1"))

#============================================#
#herança de classes

# class Top:
#     def m_top(self):
#         print("top")


# class Middle(Top):
#     def m_middle(self):
#         print("middle")


# class Bottom(Middle, Top):
#     def m_bottom(self):
#         print("bottom")


# object = Bottom()
# object.m_bottom()
# object.m_middle()
# object.m_top()


#============================================#

#herança multipla
# class Top:
#     def m_top(self):
#         print("top")


# class Middle_Left(Top):
#     def m_middle(self):
#         print("middle_left")


# class Middle_Right(Top):
#     def m_middle(self):
#         print("middle_right")


# class Bottom(Middle_Left, Middle_Right):
# 	def m_bottom(self):
# 		print("bottom")


# object = Bottom()
# object.m_bottom()
# object.m_middle()
# object.m_top()
    
#============================================#

# o metodo chamado __str__ é responsável por converter o conteúdo de um objeto em uma string (mais ou menos) legível 

# class Mouse:
#     def __init__(self, name):
#         self.my_name = name


#     def __str__(self):
#        return self.my_name


# the_mouse = Mouse('mickey')
# print(the_mouse)  # Prints "mickey".

#=============================================#

#Uma função chamadaissubclass(Classe_1, Classe_2)é capaz de determinar seClasse_1é uma subclasse deClasse_2

# class Mouse:
#     pass


# class LabMouse(Mouse):
#     pass


# print(issubclass(Mouse, LabMouse), issubclass(LabMouse, Mouse))  # Prints "False True


#=============================================#

# # Uma função chamadaisinstance(Objeto, Classe)verifica se um objeto vem de uma classe indicada . Por exemplo:

# class Mouse:
#     pass


# class LabMouse(Mouse):
#     pass


# mickey = Mouse()
# print(isinstance(mickey, Mouse), isinstance(mickey, LabMouse))  # Prints "True False".

# #==============================================#

# # Um operador chamado is verifica se duas variáveis ​​se referem ao mesmo objeto

# class Mouse:
#     pass


# mickey = Mouse()
# minnie = Mouse()
# cloned_mickey = mickey
# print(mickey is minnie, mickey is cloned_mickey)  # Prints "False True".

#==============================================#

#Uma função sem parâmetros chamadasuper()retorna uma referência à superclasse mais próxima da classe 

# class Mouse:
#     def __str__(self):
#         return "Mouse"


# class LabMouse(Mouse):
#     def __str__(self):
#         return "Laboratory " + super().__str__()


# doctor_mouse = LabMouse()
# print(doctor_mouse)  # Prints "Laboratory Mouse".

#===============================================#

#Métodos, bem como variáveis ​​de instância e de classe definidas em uma superclasse, são herdados automaticamente por suas subclasses.

# class Mouse:
#     Population = 0
#     def __init__(self, name):
#         Mouse.Population += 1
#         self.name = name

#     def __str__(self):
#         return "Hi, my name is " + self.name

# class LabMouse(Mouse):
#     pass

# professor_mouse = LabMouse("Professor Mouser")
# print(professor_mouse, Mouse.Population)  # Prints "Hi, my name is Professor Mouser 1"

#===============================================#

#Se qualquer uma das subclasses definir uma variável de método/classe/instância com o mesmo nome da existente na superclasse, o novo nome substituirá qualquer uma das instâncias anteriores do nome

# class Mouse:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return "My name is " + self.name

# class AncientMouse(Mouse):
#     def __str__(self):
#         return "Meum nomen est " + self.name

# mus = AncientMouse("Caesar")  # Prints "Meum nomen est Caesar"
# print(mus)

#======================================================

# import calendar

# c = calendar.Calendar()

# for weekday in c.iterweekdays():
#     print(weekday, end=" ")

#======================================================
# carregamento
# from time import *
# FUNDO_BRANCO = "\033[47m"
# RESET = '\033[0m'
# def carregamento_reverso():
#     for i in range (15, 0, -1):
#         e = 15 - i
#         print( f'{RESET}|{FUNDO_BRANCO}' + '' + i * ' ' ,'' + e * f'{RESET} ',f'{RESET}|', end='\r')
#         sleep(0.5)
        

# def carregamento():
#     for i in range (15):
#         e = 15 - i
#         print( f'{RESET}|{FUNDO_BRANCO}' + '' + i * ' ' + f'{RESET}','' + e * ' ', f'{RESET}|', end='\r')
#         sleep(0.5)

#======================================================

# import tkinter as tk
# import pygame as pg
# import sys

# while True:
#     escolha = input('Deseja testar:\n(1)tkinter\n(2)pygame\n(3)rich\n(4)sair\n==>').lower()
#     if escolha in ["tk","1","tkinter"]:
#         root = tk.Tk()
#         root.title("bha")

#         label = tk.Label(root, text="aoba")
#         label.pack()

#         button = tk.Button(root, text="butao")
#         button.pack

#         root.mainloop()
#     elif escolha in ["pg","2","pygame"]:
#         # Inicializa o Pygame
#         pg.init()

#         # Define o tamanho da janela
#         tela = pg.display.set_mode((800, 600))

#         # Define o título da janela
#         pg.display.set_caption("Teste Pygame")

#         # Loop principal
#         while True:
#             for evento in pg.event.get():
#                 if evento.type == pg.QUIT:
#                     pg.quit()
#                     sys.exit()

#             # Preenche a tela com uma cor
#             tela.fill((255, 0, 0))

#             # Desenha um retângulo
#             pg.draw.rect(tela, (0, 0, 255), (100, 100, 200, 200))

#             # Atualiza a tela
#             pg.display.flip()

#             # Limita a taxa de frames
#             pg.time.Clock().tick(60)
    
#     elif escolha in ['rich',"3"]:
#         from rich.table import Table
#         from rich.console import Console

#         console = Console()

#         # Cria uma tabela
#         tabela = Table(title="Teste Rich")
        
#         # Adiciona colunas à tabela
        
#         tabela.add_column("Nome", style="blue")
#         tabela.add_column("Idade", style="red")

#         # Adiciona linhas à tabela
#         tabela.add_row("João", "25")
#         tabela.add_row("Maria", "30")
    
#         console.print(tabela)
        

#     elif escolha in ["sair","4"]:
#         break

# =====================================================
### Invertendo uma string usando slicing

# palavra = "abcd"

# for i in range(len(palavra)):
#     n_palavra = palavra[::-1]


# print(n_palavra)
# =====================================================
### enumera as palavras

# frase = ['algo','de','errado','esta','errado']
# for i,palavra in enumerate(frase):
#     print(i, palavra)

# =====================================================
###bot afk 

# import pyautogui as pg
# import random as rd
# import time as tm 

# while True:
#     x = rd.randint(500, 700)
#     y = rd.randint(500, 1000)
#     pg.moveTo(x,y, 0.5)
#     tm.sleep(rd.random() * 10)

# =====================================================
### deleta uma lista de coisas de uma lista 
# a = [1,2,3,4,5]
# print(a)
# b = [2,5]
# a = list(set(a) - set(b))
# print(a)

# =====================================================
### filtra dados para nao ocorer duplicações 

# import random as rd

# letra_dict = {'A' : True,'B':True,'C':True}
# letra_list = ['A','B','C']

# letra = rd.choice(letra_list)
# print(letra)

# if letra_dict['A'] != True or letra_dict['B'] != True or letra_dict['C'] != True:
#     while letra_dict[letra] == True:
#         letra = rd.choice(letra_list)
#         print(letra)
    
# else:
#     letra = 'nada'

# print(letra)

#  =====================================================

### streamlit teste
# import streamlit as st
# import pandas as pd
# import numpy as np

# # Título da sua aplicação
# st.title('Minha Primeira Aplicação Streamlit')

# # Adicionando texto
# st.write('Olá, Streamlit! Esta é uma aplicação simples.')

# # Adicionando um slider
# idade = st.slider('Qual a sua idade?', 0, 100, 25)
# st.write(f'Sua idade é: {idade} anos.')

# # Adicionando um checkbox
# if st.checkbox('Mostrar dados aleatórios?'):
#     st.subheader('Dados Aleatórios')
#     # Criando um DataFrame com dados aleatórios
#     data = pd.DataFrame(
#         np.random.randn(10, 3),
#         columns=['col1', 'col2', 'col3']
#     )
#     st.dataframe(data) # Exibe o DataFrame

# # Adicionando um botão
# if st.button('Me clique!'):
#     st.write('Você clicou no botão!')

# # Adro (Rodapé)
# st.markdown('---') # Linha divisória
# st.write('Criado com Streamlit')

# import streamlit as st
# import pandas as pd
# import datetime

# # --- Configurações Iniciais ---
# st.set_page_config(layout="centered") # Ou "wide" para mais espaço
# st.title("Sistema de Pedidos Online")

# # --- Inicializa o carrinho de compras na session_state ---
# # O carrinho será uma lista de dicionários, cada um representando um item no pedido
# if "carrinho" not in st.session_state:
#     st.session_state.carrinho = []

# # --- Produtos disponíveis (exemplo simples) ---
# # Em um sistema real, isso viria de um banco de dados
# PRODUTOS_DISPONIVEIS = {
#     "Pizza de Calabresa": 45.00,
#     "Pizza de Mussarela": 40.00,
#     "Refrigerante Lata": 7.00,
#     "Água Mineral": 4.00,
#     "Cerveja Long Neck": 10.00
# }

# # --- Função para adicionar item ao carrinho ---
# def adicionar_ao_carrinho(produto, preco, quantidade):
#     if quantidade > 0:
#         item = {
#             "Produto": produto,
#             "Quantidade": quantidade,
#             "Preço Unit.": preco,
#             "Total Item": preco * quantidade
#         }
#         st.session_state.carrinho.append(item)
#         st.success(f"{quantidade}x {produto} adicionado(s) ao carrinho!")
#     else:
#         st.warning("A quantidade deve ser maior que zero.")

# # --- Área de Adicionar Itens ---
# st.header("Adicionar Itens ao Pedido")

# col1, col2, col3 = st.columns([3, 1, 1])

# with col1:
#     produto_selecionado = st.selectbox("Selecione o Produto", list(PRODUTOS_DISPONIVEIS.keys()))

# with col2:
#     if produto_selecionado:
#         preco_produto = PRODUTOS_DISPONIVEIS[produto_selecionado]
#         st.write(f"Preço: R$ {preco_produto:.2f}")
#     else:
#         preco_produto = 0.00 # Define um valor padrão
#         st.write("Selecione um produto")

# with col3:
#     quantidade = st.number_input("Quantidade", min_value=1, value=1, step=1)

# if st.button("Adicionar ao Carrinho"):
#     adicionar_ao_carrinho(produto_selecionado, preco_produto, quantidade)

# # --- Visualização do Carrinho ---
# st.header("Seu Carrinho")

# if st.session_state.carrinho:
#     # Cria um DataFrame do pandas para exibir o carrinho de forma tabular
#     df_carrinho = pd.DataFrame(st.session_state.carrinho)
#     st.dataframe(df_carrinho, use_container_width=True, hide_index=True)

#     # Calcula o total do pedido
#     total_pedido = df_carrinho["Total Item"].sum()
#     st.metric("Total do Pedido", f"R$ {total_pedido:.2f}")

#     # Botão para limpar o carrinho
#     if st.button("Limpar Carrinho", help="Remove todos os itens do carrinho"):
#         st.session_state.carrinho = []
#         st.rerun() # Recarrega a página para atualizar o carrinho vazio
# else:
#     st.info("Seu carrinho está vazio.")

# # --- Finalizar Pedido ---
# st.header("Finalizar Pedido")

# if st.session_state.carrinho:
#     nome_cliente = st.text_input("Seu Nome")
#     endereco_cliente = st.text_area("Endereço de Entrega")

#     if st.button("Enviar Pedido"):
#         if nome_cliente and endereco_cliente:
#             # --- Lógica de Envio do Pedido ---
#             # Aqui você salvaria o pedido em um banco de dados, enviaria um email, etc.
#             pedido_final = {
#                 "Data/Hora": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#                 "Cliente": nome_cliente,
#                 "Endereço": endereco_cliente,
#                 "Itens": st.session_state.carrinho,
#                 "Total Geral": total_pedido
#             }

#             st.success("Pedido enviado com sucesso!")
#             st.json(pedido_final) # Apenas para demonstração, exibe o JSON do pedido
#             st.balloons() # Efeitos visuais para celebrar!

#             # Opcional: Limpar o carrinho após o envio do pedido
#             st.session_state.carrinho = []
#             st.rerun() # Recarrega a página

#         else:
#             st.warning("Por favor, preencha seu nome e endereço para finalizar o pedido.")
# else:
#     st.info("Adicione itens ao carrinho antes de finalizar o pedido.")


import qrcode

# Novo link totalmente funcional (exemplo atualizado)
drive_url = "https://drive.google.com/drive/folders/1xFxX9G4vgrP2Uzv8K3yeVxRAaE9j2RZv?usp=sharing"

# Criar QR Code com esse link
qr = qrcode.make(drive_url)

# Salvar imagem
qr_path = r"C:\Users\milho\Documents\cod_programacao\qr_code_final_23311425.png"
qr.save(qr_path)

qr_path