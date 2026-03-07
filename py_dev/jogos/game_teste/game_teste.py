import pygame as pg

pg.init()

largura_tela = 800
altura_tela = 600
tela = pg.display.set_mode((largura_tela, altura_tela))


pg.display.set_caption("Meu Primeiro Jogo Pygame")

BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
VERDE = (0,255,0)

pos_x_jogador = largura_tela // 2
pos_y_jogador = altura_tela // 2
tamanho_jogador_y = 50
tamanho_jogador_x = 50
velocidade_jogador = 5

rodando = True
while rodando:
    # 1. Eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT: # Se o usuário clicar no 'X' para fechar
            rodando = False
        elif evento.type == pg.KEYDOWN: # Se uma tecla for pressionada
            if evento.key == pg.K_a:
                pos_x_jogador -= velocidade_jogador
            elif evento.key == pg.K_d:
                pos_x_jogador += velocidade_jogador
            elif evento.key == pg.K_w:
                pos_y_jogador -= velocidade_jogador
            elif evento.key == pg.K_s:
                pos_y_jogador += velocidade_jogador

    # 2. Atualizações do jogo (lógica)
    # Garante que o jogador não saia da tela
    pos_x_jogador = max(0, min(pos_x_jogador, largura_tela - tamanho_jogador_x))
    pos_y_jogador = max(0, min(pos_y_jogador, altura_tela - tamanho_jogador_y))

    # 3. Desenho (renderização)
    tela.fill(BRANCO) # Preenche o fundo da tela de branco

    # Desenha o jogador (um retângulo azul)
    pg.draw.rect(tela, AZUL, (pos_x_jogador, pos_y_jogador, tamanho_jogador_x, tamanho_jogador_y))

    # Atualiza a tela para exibir o que foi desenhado
    pg.display.flip()

pg.quit()
print("Jogo Pygame encerrado.")