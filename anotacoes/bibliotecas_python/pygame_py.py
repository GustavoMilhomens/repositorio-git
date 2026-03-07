
# 10. Biblioteca pygame
# A biblioteca pygame é um conjunto de módulos Python projetados para escrever jogos. Ela fornece funcionalidade para gráficos, som, entrada do usuário e muito mais.
#  * Não é uma biblioteca nativa.
#  * Para instalar, use: pip install pygame
#  * Geralmente importada como import pygame.
# <!-- end list -->
import pygame

# Inicializa todos os módulos Pygame necessários
pygame.init()

# Define as dimensões da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Define o título da janela
pygame.display.set_caption("Meu Primeiro Jogo Pygame")

# Define cores (RGB)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

# Posição e tamanho do jogador (um quadrado)
pos_x_jogador = largura_tela // 2
pos_y_jogador = altura_tela // 2
tamanho_jogador = 50
velocidade_jogador = 5

# Loop principal do jogo
rodando = True
while rodando:
    # 1. Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # Se o usuário clicar no 'X' para fechar
            rodando = False
        elif evento.type == pygame.KEYDOWN: # Se uma tecla for pressionada
            if evento.key == pygame.K_LEFT:
                pos_x_jogador -= velocidade_jogador
            elif evento.key == pygame.K_RIGHT:
                pos_x_jogador += velocidade_jogador
            elif evento.key == pygame.K_UP:
                pos_y_jogador -= velocidade_jogador
            elif evento.key == pygame.K_DOWN:
                pos_y_jogador += velocidade_jogador

    # 2. Atualizações do jogo (lógica)
    # Garante que o jogador não saia da tela
    pos_x_jogador = max(0, min(pos_x_jogador, largura_tela - tamanho_jogador))
    pos_y_jogador = max(0, min(pos_y_jogador, altura_tela - tamanho_jogador))

    # 3. Desenho (renderização)
    tela.fill(BRANCO) # Preenche o fundo da tela de branco

    # Desenha o jogador (um retângulo azul)
    pygame.draw.rect(tela, AZUL, (pos_x_jogador, pos_y_jogador, tamanho_jogador, tamanho_jogador))

    # Atualiza a tela para exibir o que foi desenhado
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
print("Jogo Pygame encerrado.")

######################################################

# # link com mais informações
#  * pygame:
#    https://www.pygame.org/docs/