# criação de site com IA

# titulo
# input chat 
# cada mensagem enviada :
   # mostra a mensagem que o usuario emviou no chat
   # enviar essa mensagem para a IA responder
   # aparecer na tela a resposta da IA

# streamlit - frontend e backand
# streamlit run site.py
# streamlit run C:\Users\milho\Documents\cod_programacao\aula_jornada_python\aula4\site.py
import streamlit as st

st.write('Chatbot com IA')

if not "lista_mensagens" in st.session_state:
   st.session_state["lista_mensagens"] = []

# exibir o historico de mensagem
for mensagem in st.session_state['lista_mensagens']:
   role = mensagem['role']
   content = mensagem['content']

   st.chat_message(role).write(content)


mensagem_usuario = st.chat_input('Digite sua mensagem')

if mensagem_usuario:
   # user -> ser humano
   # assistent -> IA

   st.chat_message('user').write(mensagem_usuario)
   mensagem = {"role": "user", "content": mensagem_usuario} # armazena as mensagens
   st.session_state["lista_mensagens"].append(mensagem)
   # resposta da IA
   resposta_ia = 'você disse : ' + mensagem_usuario + '?'

   # exibir a resposta da IA
   st.chat_message('assistant').write(resposta_ia)
   
   mensagem_ai = {"role": "user", "content": resposta_ia} 
   st.session_state["lista_mensagens"].append(mensagem_ai)

   print(st.session_state['lista_mensagens'])

   
