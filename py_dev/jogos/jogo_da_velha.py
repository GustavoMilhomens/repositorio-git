#Jogo da velha com matriz
from random import*
from time import*

def pontos(interv):
    for i in range(interv):
        print(".  ",sep=sleep(0.3),end='\r')
        print(".. ",sep=sleep(0.3),end='\r')
        print("...",sep=sleep(0.3),end='\r')
        print("   ",sep=sleep(0.1),end='\r')

def interface(p1,p2,p3,p4,p5,p6,p7,p8,p9):
    return print(f'  0 1 2\n0 {p1}|{p2}|{p3}\n1 {p4}|{p5}|{p6}\n2 {p7}|{p8}|{p9}')

def vencedor():
    if posicoes[0][0]== 'x' and posicoes[0][1]== 'x' and posicoes[0][2] == 'x' or posicoes[1][0]== 'x' and posicoes[1][1]== 'x' and posicoes[1][2]== 'x' or posicoes[2][0]== 'x' and posicoes[2][1]== 'x' and posicoes[2][2] == 'x':
        resul='"x" venceu'
    elif posicoes[0][0]== 'x' and posicoes[1][0]== 'x' and posicoes[2][0] == 'x' or posicoes[0][1]== 'x' and posicoes[1][1]== 'x' and posicoes[2][1]== 'x' or posicoes[0][2]== 'x' and posicoes[1][2]== 'x' and posicoes[2][2] == 'x':
        resul='"x" venceu'
    elif posicoes[0][0]== 'x' and posicoes[1][1]== 'x' and posicoes[2][2] == 'x' or posicoes[0][2]== 'x' and posicoes[1][1]== 'x' and posicoes[2][0] == 'x':
        resul='"x" venceu'
    elif posicoes[0][0]== 'o' and posicoes[0][1]== 'o' and posicoes[0][2] == 'o' or posicoes[1][0]== 'o' and posicoes[1][1]== 'o' and posicoes[1][2]== 'o' or posicoes[2][0]== 'o' and posicoes[2][1]== 'o' and posicoes[2][2] == 'o':
        resul='"o" venceu'
    elif posicoes[0][0]== 'o' and posicoes[1][0]== 'o' and posicoes[2][0] == 'o' or posicoes[0][1]== 'o' and posicoes[1][1]== 'o' and posicoes[2][1]== 'o' or posicoes[0][2]== 'o' and posicoes[1][2]== 'o' and posicoes[2][2] == 'o':
        resul='"o" venceu'
    elif posicoes[0][0]== 'o' and posicoes[1][1]== 'o' and posicoes[2][2] == 'o' or posicoes[0][2]== 'o' and posicoes[1][1]== 'o' and posicoes[2][0] == 'o':
        resul='"o" venceu'
    else:
        resul='deu velha'
    return resul
    
    
def posicionar(sinal):
    linCol=input(f'Informe a linha e a coluna de "{sinal}"\n==>')
    
    #erro de velor e quantidade
    while True:
        try:
            lin=int(linCol[0])
            col=int(linCol[1])
            #erro de ocupação de lugar
            while posicoes[lin][col] in ['x','o']:
                print('Posição ocupada\nTente novamente\n')
                linCol=input(f'Informe a linha e a coluna de "{sinal}"\n==>')
                lin=int(linCol[0])
                col=int(linCol[1])
            break
            
        except IndexError:
            print('Erro\nInforme 2 valores inteiros entre 0 e 2')
            linCol=input(f'Informe a linha e a coluna de "{sinal}"\n==>')
        except ValueError:
            print('Erro\nValor incompativel')
            linCol=input(f'Informe a linha e a coluna de "{sinal}"\n==>')
    
        
    posicoes[lin][col]=sinal
    interface(posicoes[0][0],posicoes[0][1],posicoes[0][2],posicoes[1][0],posicoes[1][1],posicoes[1][2],posicoes[2][0],posicoes[2][1],posicoes[2][2])



#posicoes=[[1,2,3],[4,5,6],[7,8,9]]

while True:
    posicoes=[[1,2,3],[4,5,6],[7,8,9]]
    i=0
    op=input('\nDeseja jogas:\n1)jogador vs jogador\n2)máquina vs jogador\n3)sair\n==> ')
    
    #jogador contra jogador 
    if op == '1':
        interface(posicoes[0][0],posicoes[0][1],posicoes[0][2],posicoes[1][0],posicoes[1][1],posicoes[1][2],posicoes[2][0],posicoes[2][1],posicoes[2][2])
        while True:
            i=i+1
            posicionar('x')
            if i==5 or vencedor() != 'deu velha':
                print(vencedor())
                break 
            posicionar('o')
            
        
    # jogador e máquina     
    elif op == '2':
        interface(posicoes[0][0],posicoes[0][1],posicoes[0][2],posicoes[1][0],posicoes[1][1],posicoes[1][2],posicoes[2][0],posicoes[2][1],posicoes[2][2])
        pontos(1)
        print('"x" na podicao 11')
        posicoes[1][1]='x'
        while True:
            i=i+1
            interface(posicoes[0][0],posicoes[0][1],posicoes[0][2],posicoes[1][0],posicoes[1][1],posicoes[1][2],posicoes[2][0],posicoes[2][1],posicoes[2][2])
            posicionar('o')
            
            pontos(2)
            lin=choice(0,1,2)
            col=choice(0,1,2)
            while posicoes[lin][col] in ['x','o']:
                pontos(1)
                lin=choice(0,1,2)
                col=choice(0,1,2)
            print(f'"x" na posição {lin}{col}')    
            posicoes[lin][col]='x'
            
            if i==5 or vencedor() != 'deu velha':
                print(vencedor())
                break 
    #sair
    elif op == "3":
        print('Saindo do sistema')
        pontos(2)
        break
    
    # erro de opção inesistente 
    else:
        print('Erro \nOpção inesistente')