# 1. Biblioteca time
# A biblioteca time fornece funções para trabalhar com tempo. É útil para pausar a execução de um programa, medir a duração de operações ou obter a data e hora atuais.
#  * É uma biblioteca nativa do Python.
#  * Não precisa de instalação.
#  * Não possui um nome comumente atribuído na importação, geralmente importada como import time.
# <!-- end list -->
import time

# time.sleep(segundos)
# Pausa a execução do programa pelo número de segundos especificado.
print("Esperando 3 segundos...")
time.sleep(3)
print("3 segundos se passaram!")

# time.time()
# Retorna o tempo atual em segundos desde a "Epoch" (1º de janeiro de 1970, 00:00:00 UTC).
inicio = time.time()
print(f"Início da operação: {inicio} segundos")
time.sleep(2)
fim = time.time()
duracao = fim - inicio
print(f"Fim da operação: {fim} segundos")
print(f"A operação durou {duracao:.2f} segundos.")

######################################################

# link com mais informações 
#  * time (Python Standard Library):
#    https://docs.python.org/3/library/time.html