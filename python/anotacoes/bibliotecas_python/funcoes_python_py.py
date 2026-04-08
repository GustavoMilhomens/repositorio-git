
# 12. Algumas Funções Nativas do Python
# Além das bibliotecas, o Python possui diversas funções e recursos que já vêm "embutidos" (built-in) e são essenciais para o dia a dia da programação.
#  * São funções nativas do Python.
#  * Não precisam de instalação nem importação.
# <!-- end list -->
# print()
# Exibe informações na console. É a função mais básica para depuração e saída.
print("Olá, Python!")
print("O valor de 2 + 2 é:", 2 + 2)

# input(mensagem)
# Lê entrada do usuário a partir do teclado. Retorna uma string.
# nome_usuario = input("Qual é o seu nome? ")
# print(f"Prazer em conhecê-lo, {nome_usuario}!")

# len(objeto)
# Retorna o número de itens em um objeto (string, lista, tupla, dicionário, etc.).
minha_lista = [10, 20, 30, 40]
print(f"O comprimento da lista é: {len(minha_lista)}")
minha_string = "Python"
print(f"O comprimento da string é: {len(minha_string)}")

# type(objeto)
# Retorna o tipo de um objeto.
numero = 123
texto = "abc"
print(f"O tipo de {numero} é: {type(numero)}")
print(f"O tipo de '{texto}' é: {type(texto)}")

# int(), float(), str(), bool()
# Funções de conversão de tipo (casting).
numero_str = "123"
numero_int = int(numero_str)
print(f"'{numero_str}' como inteiro: {numero_int} (Tipo: {type(numero_int)})")

decimal_str = "3.14"
decimal_float = float(decimal_str)
print(f"'{decimal_str}' como float: {decimal_float} (Tipo: {type(decimal_float)})")

inteiro = 42
inteiro_str = str(inteiro)
print(f"{inteiro} como string: '{inteiro_str}' (Tipo: {type(inteiro_str)})")

# min(), max(), sum()
# Funções para sequências de números.
numeros = [5, 1, 9, 3, 7]
print(f"Menor número: {min(numeros)}")
print(f"Maior número: {max(numeros)}")
print(f"Soma dos números: {sum(numeros)}")

# range(inicio, fim, passo)
# Gera uma sequência de números, comumente usada em loops for.
print("Números de 0 a 4:")
for i in range(5): # Começa em 0, vai até 5 (exclusive)
    print(i)

print("Números de 2 a 8 (pulando de 2 em 2):")
for i in range(2, 9, 2):
    print(i)


######################################################

# # link com mais informações
#  * Funções Nativas (Built-in Functions) do Python:
#    https://docs.python.org/3/library/functions.html