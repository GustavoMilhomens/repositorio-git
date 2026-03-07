# 2. Biblioteca calendar
# A biblioteca calendar fornece funções para trabalhar com calendários, como imprimir calendários de meses ou anos e obter informações sobre dias da semana.
#  * É uma biblioteca nativa do Python.
#  * Não precisa de instalação.
#  * Não possui um nome comumente atribuído na importação, geralmente importada como import calendar.
# <!-- end list -->
import calendar

# calendar.month(ano, mes)
# Retorna o calendário de um mês específico em formato de string.
print(calendar.month(2025, 7))

# calendar.calendar(ano)
# Retorna o calendário de um ano inteiro em formato de string.
print(calendar.calendar(2025))

# calendar.weekday(ano, mes, dia)
# Retorna o dia da semana para uma data específica (0=segunda, 6=domingo).
dia_semana = calendar.weekday(2025, 7, 14)
print(f"14 de julho de 2025 é o dia {dia_semana} da semana (0=segunda-feira).")

# calendar.isleap(ano)
# Verifica se um ano é bissexto.
print(f"2024 é um ano bissexto? {calendar.isleap(2024)}")
print(f"2025 é um ano bissexto? {calendar.isleap(2025)}")

######################################################

# # link com mais informações
#  * calendar (Python Standard Library):
#    https://docs.python.org/3/library/calendar.html