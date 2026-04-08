# comando para ativar o site: streamlit run teste_py.py

import streamlit as st
import random as rd

st.set_page_config(layout="centered")
st.title('Val bolos') # titulo do site

if 'pedidos' not in st.session_state: # armazena os dados em uma lista de dicionario 
    st.session_state.pedidos = []

tipos_bolos = {'esolha o bolo':0.00,
            'bolo de aniversario' : 65.00,
            'bolo caseiro' : 50.00,
            'bolo caseiro com cobertura' : 60.00,
            'bolo de aniversario de andar' : 65.00
}
recheios = ['esolha o recheio',
            'Leite ninho'  ,
            'Brigadeiro' , 
            'Ouro branco' ,
            'Sonho de valsa' ,
            'Coco' ,
            'Prestígio'  ,
            'Musse de maracujá', 
            'Leite condensado', 
            'Abacaxi' , 
            'Quatro leite' ]
massas = ['escolha uma massa de bolo','chocolate','pão de ló']

st.header('Olá, oque deseja?') # escreve algo na tela


coluna1, coluna2, coluna3, = st.columns([3,2,2]) # cria 3 colunas

with coluna1:  # cria uma area para escolher o tipo do bolo
    tipo_bolo_escolhido = st.selectbox('informe o tipo do bolo', list(tipos_bolos.keys())) 
    # cria uma caixa para escolher 

with coluna1: # arae para escolher a massa do bolo
    if tipo_bolo_escolhido == ['bolo caseiro','bolo caseiro com cobertura']:
        massa_bolo = st.selectbox(f'massa disponivel para {tipo_bolo_escolhido}', 'chocolate')
    else :
        massa_bolo = st.selectbox(f'massa disponivel para {tipo_bolo_escolhido}', massas)

with coluna2: # coloca para escolher o peso do bolo
    if tipo_bolo_escolhido == 'bolo de aniversario de andar':
        peso = st.number_input("Pesso em kg", min_value=3, value=3, step=1)
    else:
        peso = st.number_input("Pesso em kg", min_value=1, value=1, step=1)

with coluna3: # escolhe o recheio
    recheio_escolhido1 = st.selectbox('informe o primeiro recheio', recheios)

with coluna3:
    recheio_escolhido2 = st.selectbox('informe o segundo recheio', recheios)

# mostra o preço do bolo 
with coluna2:
    if tipo_bolo_escolhido: # se a variavel tiver alggo o sistema mostra o valor
        preco_bolo = tipos_bolos[tipo_bolo_escolhido] * peso
        st.write(f"Preço: R$ {preco_bolo:.2f}")
    else:
        preco_bolo = 0.00 
        st.write("Selecione um produto")

# comfrma o pedido
with coluna1:
    if st.button('fazer pedido'):
        id_cliente =  rd.randint(1,100) # isso é provisorio
        dados = "\n" + str(id_cliente) + ',' + str(tipo_bolo_escolhido) + ',' + str(massa_bolo) + ',' + str(peso) + ',' + str(recheio_escolhido1) + ',' + str(recheio_escolhido2)

        with open('base_dados.csv','a') as file:
            if "None" in dados:
                print('tem None')
            
            elif 'esolha o bolo' in dados or 'esolha o recheio' in dados or 'escolha uma massa de bolo' in dados :
                st.write('falta dados')

            else:
                file.write(dados) 
                st.write('pedido feito') 

        

