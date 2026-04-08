
# 8. Biblioteca tkinter
# A biblioteca tkinter é o toolkit padrão do Python para criar interfaces gráficas de usuário (GUIs) desktop. É simples e nativa, ideal para aplicações pequenas e médias.
#  * É uma biblioteca nativa do Python.
#  * Não precisa de instalação (geralmente já vem com o Python).
#  * Geralmente importada como import tkinter as tk.
# <!-- end list -->
import tkinter as tk
from tkinter import messagebox # Importa o módulo de caixas de mensagem


# Cria a janela principal da aplicação
janela = tk.Tk()
janela.title("Meu Primeiro App Tkinter")
janela.geometry("400x300") # Define o tamanho da janela

# Função para ser chamada quando o botão for clicado
def saudacao():
    nome = entrada_nome.get() # Pega o texto da caixa de entrada
    if nome:
        messagebox.showinfo("Saudação", f"Olá, {nome}!")
    else:
        messagebox.showwarning("Aviso", "Por favor, digite seu nome!")

# Criando um Label (rótulo de texto)
label_instrucao = tk.Label(janela, text="Digite seu nome:")
label_instrucao.pack(pady=10) # .pack() organiza o widget na janela

# Criando uma Entry (caixa de entrada de texto)
entrada_nome = tk.Entry(janela, width=30)
entrada_nome.pack(pady=5)

# Criando um Button (botão)
botao_saudacao = tk.Button(janela, text="Saudar", command=saudacao)
botao_saudacao.pack(pady=10)

# Criando um Label para exibir feedback
label_feedback = tk.Label(janela, text="")
label_feedback.pack(pady=5)

# Função para atualizar o feedback quando o texto da entrada muda (exemplo avançado)
def atualizar_feedback(event=None):
    texto_atual = entrada_nome.get()
    label_feedback.config(text=f"Você digitou: {texto_atual}")

entrada_nome.bind("<KeyRelease>", atualizar_feedback) # Liga a função a um evento de teclado

# Inicia o loop principal da aplicação (mantém a janela aberta)
janela.mainloop()

######################################################

# # link com mais informações
#  * tkinter (Python Standard Library):
#    https://docs.python.org/3/library/tkinter.html