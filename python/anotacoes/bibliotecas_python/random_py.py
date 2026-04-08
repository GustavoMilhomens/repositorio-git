
# 4. Biblioteca random
# A biblioteca random é usada para gerar números pseudoaleatórios. É útil para simulações, jogos, seleção aleatória de elementos e embaralhamento.
#  * É uma biblioteca nativa do Python.
#  * Não precisa de instalação.
#  * Não possui um nome comumente atribuído na importação, geralmente importada como import random.
# <!-- end list -->
import random

# random.randint(a, b)
# Retorna um inteiro aleatório N tal que a <= N <= b.
numero_aleatorio_int = random.randint(1, 10)
print(f"Número inteiro aleatório entre 1 e 10: {numero_aleatorio_int}")

# random.random()
# Retorna um float aleatório entre 0.0 (inclusive) e 1.0 (exclusive).
numero_aleatorio_float = random.random()
print(f"Número float aleatório entre 0.0 e 1.0: {numero_aleatorio_float:.2f}")

# random.choice(sequencia)
# Retorna um elemento aleatório de uma sequência (lista, tupla, string).
lista_frutas = ["maçã", "banana", "cereja", "laranja"]
fruta_escolhida = random.choice(lista_frutas)
print(f"Fruta escolhida aleatoriamente: {fruta_escolhida}")

# random.shuffle(lista)
# Embaralha (muda a ordem no local) os itens de uma lista.
cartas = ["Ás", "Rei", "Rainha", "Valete"]
random.shuffle(cartas)
print(f"Cartas embaralhadas: {cartas}")

######################################################

# # link com mais informações
#  * random (Python Standard Library):
#    https://docs.python.org/3/library/random.html