
# 7. Biblioteca pyautogui
# A biblioteca pyautogui permite automatizar a interface gráfica do usuário (GUI), controlando o mouse e o teclado. É útil para automação de tarefas repetitivas em aplicativos de desktop.
#  * Não é uma biblioteca nativa.
#  * Para instalar, use: pip install pyautogui
#  * Não possui um nome comumente atribuído na importação, geralmente importada como import pyautogui.
# Cuidado: Ao usar pyautogui, seu computador será controlado pelo script. Tenha um plano para interromper o script (geralmente movendo o mouse para um dos quatro cantos da tela rapidamente ou pressionando Ctrl+C no terminal).
import pyautogui
import time

# pyautogui.size()
# Retorna a largura e altura da tela.
largura, altura = pyautogui.size()
print(f"Resolução da tela: Largura={largura}, Altura={altura}")

# pyautogui.position()
# Retorna a posição X, Y atual do mouse.
pos_mouse = pyautogui.position()
print(f"Posição atual do mouse: {pos_mouse}")

# pyautogui.moveTo(x, y, duration=segundos)
# Move o mouse para uma posição X, Y na tela.
print("Movendo o mouse para o centro da tela em 2 segundos...")
pyautogui.moveTo(largura / 2, altura / 2, duration=2)
time.sleep(1) # Pequena pausa para observar

# pyautogui.click(x, y)
# Clica com o botão esquerdo do mouse na posição X, Y.
# Cuidado: Esta função realmente clica onde você especificar!
# print("Clicando no centro da tela...")
# pyautogui.click(largura / 2, altura / 2)

# pyautogui.typewrite(texto, interval=segundos)
# Digita uma string de texto.
print("Digitando 'Olá, PyAutoGUI!' em um campo de texto (se houver um focado)...")
# Certifique-se de ter um campo de texto ativo (ex: bloco de notas, navegador) antes de rodar isso.
# pyautogui.typewrite("Olá, PyAutoGUI!", interval=0.1)

# pyautogui.press(tecla)
# Pressiona uma tecla.
# print("Pressionando a tecla 'enter'...")
# pyautogui.press('enter')

# pyautogui.hotkey(tecla1, tecla2, ...)
# Pressiona uma combinação de teclas (ex: Ctrl+C, Alt+Tab).
# print("Pressionando Ctrl+Shift+Esc para abrir o Gerenciador de Tarefas (Windows)...")
# pyautogui.hotkey('ctrl', 'shift', 'esc')

######################################################

# # link com mais informações
#  * pyautogui:
#    https://pyautogui.readthedocs.io/