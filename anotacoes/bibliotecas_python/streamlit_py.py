
# 5. Biblioteca streamlit
# A biblioteca streamlit é uma ferramenta de código aberto para criar rapidamente aplicativos web interativos para ciência de dados e machine learning, tudo usando Python puro.
#  * Não é uma biblioteca nativa.
#  * Para instalar, use: pip install streamlit
#  * Não possui um nome comumente atribuído na importação, geralmente importada como import streamlit as st.
# Para usar o Streamlit:
#  * Crie um arquivo Python (ex: app.py).
#  * Escreva seu código Streamlit.
#  * Execute no terminal: streamlit run app.py
# <!-- end list -->
# app.py (Este é o conteúdo do arquivo que você criaria)

import streamlit as st

# st.title(texto)
# Adiciona um título ao seu aplicativo.
st.title("Meu Primeiro App Streamlit")

# st.header(texto)
# Adiciona um cabeçalho.
st.header("Boas-vindas!")

# st.write(conteudo)
# Escreve texto, dataframes, gráficos, etc.
st.write("Este é um aplicativo simples criado com Streamlit.")

# st.button(label)
# Adiciona um botão e retorna True se clicado.
if st.button("Clique-me!"):
    st.write("Botão clicado!")

# st.slider(label, min_value, max_value)
# Adiciona um slider para selecionar um valor numérico.
valor = st.slider("Escolha um número", 0, 100, 25)
st.write(f"Você escolheu: {valor}")

# st.text_input(label)
# Adiciona um campo de entrada de texto.
nome = st.text_input("Qual é o seu nome?")
if nome:
    st.write(f"Olá, {nome}!")

# st.sidebar
# Adiciona conteúdo à barra lateral.
st.sidebar.title("Opções")
st.sidebar.write("Esta é a barra lateral.")

# st.dataframe(data)
# Exibe um DataFrame do Pandas (necessita Pandas instalado).
# import pandas as pd
# data = {'Coluna A': [1, 2, 3], 'Coluna B': [4, 5, 6]}
# df = pd.DataFrame(data)
# st.dataframe(df)

# Para rodar este exemplo:
# 1. Salve o código acima em um arquivo chamado app.py.
# 2. Abra o terminal na mesma pasta onde salvou o arquivo.
# 3. Digite streamlit run app.py e pressione Enter.
# 4. Seu navegador padrão abrirá o aplicativo.

######################################################

# # link com mais informações
#  * streamlit:
#    https://docs.streamlit.io/
