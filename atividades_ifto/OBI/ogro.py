# prova teste da Olimpiada Brasileira de Informatica(OBI) de 2025

# se o número de dedos na mão esquerda é maior do que o número de dedos na mão direita (ou
# seja E > D) então o resultado é a soma dos dois números (ou seja E + D);
#  caso contrário, o resultado é o dobro da diferença entre o número de dedos na mão direita e
# o número de dedos na mão esquerda (ou seja, 2 × (D − E)).

n_dedos_esq = int(input("mão esq: "))
n_dedos_dir = int(input('mão dir: '))
if n_dedos_esq > n_dedos_dir:
    print( n_dedos_esq + n_dedos_dir)

else:
    print( 2*(n_dedos_dir - n_dedos_esq))

