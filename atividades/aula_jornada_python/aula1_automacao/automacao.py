# passo 1 : entrar no site https://dlp.hashtagtreinamentos.com/python/intensivao/login
# passo 2 : fazer login com o usuário e senha
# passo 3 : importar base de dados 
# passo 4 : cadastrar 1 produto 
# passo 5 : repetir ´para todos os produtos 

# caso queira saber mais pesquise pyautogui python 

import time  # Importa o módulo time para usar sleep
import pyautogui # serve para automatizar o mouse e o teclado
import pandas



# while True:
#     print(pyautogui.position())  # Imprime a posição atual do mouse
#     time.sleep(1)  # Aguarda 1 segundo antes de imprimir novamente



# click = clica em um local especifico da tela
# moveTo = move o mouse para um local especifico da tela
# press = presiona uma unica tecla 
# write = escreve um texto
# hotkey = pressiona varias teclas ao mesmo tempo
# PAUSE = pausa a execução do script por um tempo especifico
# posicion = retorna a posição atual do mouseBOHA000252
# moveTo = move o mouse para uma posição especifica


# precisa de um delei entre alguns comandos 
# para executar melhor ou carregar a pagina

pyautogui.PAUSE = 2  # Define um atraso de 1 segundo entre os comandos



# Passo 1: Abrir o navegador Chrome e acessar a URL
# pyautogui.hotkey('win', 'd')  # Minimiza todas as janelas
pyautogui.press('win')  # Pressiona a tecla do Windows
pyautogui.write('chrome')  # Digita "chrome"
pyautogui.press('enter')  # Pressiona Enter para abrir o Chrome
time.sleep(2)
pyautogui.click(x=870, y=594)
time.sleep(2)  # Aguarda 2 segundos para o Chrome abrir
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')  # Digita a URL
time.sleep(4)
pyautogui.press('enter')  # Pressiona Enter para acessar a URL123456

# Passo 2: Fazer login com o usuário e senha
pyautogui.press('tab')
# 6.5   Logitechpyautogui.click(x=1175, y=434) # Clica no campo de usuário
pyautogui.write('gustavo')  # Digita o usuário
time.sleep(1)  # Aguarda 1 segundo
pyautogui.press('tab') # Clica no campo de senha
# pyautogui.press('tab')  # Pressiona Tab para ir para o campo de senha
pyautogui.write('123456')  # Digita a senhaMOLO000251   
time.sleep(1)  # Aguarda 1 segundo
# pyautogui.press('tab')
pyautogui.press('enter')  # Clica no botão de login
time.sleep(4)  # Aguarda 4 segundos para o login ser processado
pyautogui.click(x=1690, y=458) 

# Passo 3: Importar a base de dados

# se o arquivo estiver na mesma pasta do script, pode usar o caminho relativo
# Se estiver em outra pasta, use o caminho absoluto
tabela = pandas.read_csv('C:/Users/milho/Documents/cod_programacao/aula_jornada_python/aula1/produtos.csv')  # Lê o arquivo CSV com os produtos
print(tabela)

# Passo 4: cadastrar produtos
# coloca somente um produto

# codigo = 'MOLO000251'
# marca = 'Logitech'
# tipo = 'Mouse'  
# categoria = '1'
# preco_unitario = '25.95' 
# custo = '6.50'
# obs = ''



# pyautogui.click(x=1234, y=302) # clicar no codigo de produtos 
# pyautogui.write(codigo)  # Digita o código do produto
# pyautogui.press('tab') # clicar no marca do produto
# pyautogui.write(marca)  # Digita a marca do produto
# pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
# pyautogui.write(tipo)  # Digita o tipo do produto
# pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
# pyautogui.write(categoria)  # Digita a categoria do produto
# pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
# pyautogui.write(preco_unitario)  # Digita o preço unitário do produto
# pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
# pyautogui.write(custo)  # Digita o custo do produto
# pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
# pyautogui.write(obs)  # Digita a observação do produto
# pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
# pyautogui.press('enter')  # Pressiona Enter para cadastrar o produto

# pyautogui.scroll(10000) # rola para o topo da página



# Passo 5: Repetir para todos os produtos
# coloca todos os produtos da tabela
# para plausar a automação coloca o mause no topo da tela 

for linha in tabela.index:
    codigo = tabela.loc[linha, 'codigo'] # loc localisa, só funcionam com colhetes
    marca = tabela.loc[linha, 'marca']
    tipo = tabela.loc[linha, 'tipo']  
    categoria = str(tabela.loc[linha, 'categoria']) # se colocar numero vai dar erro
    preco_unitario = str(tabela.loc[linha, 'preco_unitario']) # para colocar em string usa str
    custo = str(tabela.loc[linha, 'custo']) # string é texto
    obs = str(tabela.loc[linha, 'obs']) # da erro pq o write só aceita string

    pyautogui.click(x=1234, y=302)  # Clica no campo de código de produtos
    pyautogui.write(codigo)  # Digita o código do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    pyautogui.write(marca)  # Digita a marca do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    pyautogui.write(tipo)  # Digita o tipo do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    pyautogui.write(categoria)  # Digita a categoria do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    pyautogui.write(preco_unitario)  # Digita o preço unitário do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    pyautogui.write(custo)  # Digita o custo do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    if obs != 'nan': # Verifica se a observação não é nula
        pyautogui.write(obs)  # Digita a observação do produto

    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    pyautogui.press('enter')  # Pressiona Enter para cadastrar o produto

# nan = not a number, é um valor nulo








