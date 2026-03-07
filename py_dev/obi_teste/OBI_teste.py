from collections import deque

def resolver_resgate_robo(N, M, grid):
    # Encontrar a posição inicial de R e E
    start_r, start_c = -1, -1
    end_r, end_c = -1, -1
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 'R':
                start_r, start_c = r, c
            elif grid[r][c] == 'E':
                end_r, end_c = r, c

    # Inicializa as matrizes de distância (tempo) e minas
    # Usamos N*M + 1 como "infinito" para tempo e minas para garantir que qualquer caminho será menor
    # (N*M é o número máximo de células, então o tempo máximo sem minas é N*M-1)
    # A escolha de 200*200 para minas é um "infinito" prático, já que o máximo de minas é N*M
    distancias = [[float('inf')] * M for _ in range(N)]
    minas_minimas = [[float('inf')] * M for _ in range(N)]

    # Fila para a BFS: (linha, coluna, tempo_atual, minas_pisadas_atuais)
    fila = deque()

    # Posição inicial de R.E.X.
    # Tempo inicial é 0, minas pisadas é 0
    distancias[start_r][start_c] = 0
    minas_minimas[start_r][start_c] = 0
    fila.append((start_r, start_c, 0, 0))

    # Direções de movimento (cima, baixo, esquerda, direita)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while fila:
        r, c, tempo_atual, minas_atuais = fila.popleft()

        # Se chegamos ao destino, podemos parar para este caminho,
        # mas a BFS garante que a primeira vez que chegamos, é o caminho mais curto em tempo
        # A min_minas no ponto E já terá sido atualizada pelo caminho ótimo.
        # No entanto, a BFS continua explorando para garantir que, para o mesmo tempo,
        # encontremos o menor número de minas.

        # Explorar vizinhos
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            # Verificar limites da grade
            if 0 <= nr < N and 0 <= nc < M:
                # Não pode passar por obstáculos
                if grid[nr][nc] == '#':
                    continue

                novo_tempo = tempo_atual + 1
                novas_minas = minas_atuais
                if grid[nr][nc] == 'M': # Se pisar em uma mina, incrementa
                    novas_minas += 1

                # Condições de atualização:
                # 1. Encontrou um caminho mais rápido
                if novo_tempo < distancias[nr][nc]:
                    distancias[nr][nc] = novo_tempo
                    minas_minimas[nr][nc] = novas_minas
                    fila.append((nr, nc, novo_tempo, novas_minas))
                # 2. Encontrou um caminho com o mesmo tempo, mas com menos minas
                elif novo_tempo == distancias[nr][nc] and novas_minas < minas_minimas[nr][nc]:
                    minas_minimas[nr][nc] = novas_minas
                    # É importante adicionar à fila novamente, pois um caminho com menos minas
                    # a partir deste ponto pode levar a melhores resultados futuros.
                    fila.append((nr, nc, novo_tempo, novas_minas))

    # Após a BFS, o valor em minas_minimas[end_r][end_c] será a resposta
    if minas_minimas[end_r][end_c] == float('inf'):
        return -1 # Não foi possível alcançar o ponto de extração
    else:
        return minas_minimas[end_r][end_c]

# --- Exemplo de Uso ---
# N, M para o Exemplo 1
# N, M = 4, 5
# grid_exemplo1 = [
#     "R.M..",
#     ".#.M.",
#     ".#...",
#     "...E."
# ]
# print(resolver_resgate_robo(N, M, grid_exemplo1)) # Saída esperada: 1

# N, M para o Exemplo 2
# N, M = 3, 3
# grid_exemplo2 = [
#     "R.M",
#     ".#.",
#     ".ME"
# ]
# print(resolver_resgate_robo(N, M, grid_exemplo2)) # Saída esperada: 2

