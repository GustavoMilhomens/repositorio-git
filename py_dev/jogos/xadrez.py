RESET = '\033[0m'
LINHA = '\033[4m'



def inter(posicao):
    return f"""{LINHA}
                                  _
8 | {posicao[7][0]} | {posicao[7][1]} | {posicao[7][2]} | {posicao[7][3]} | {posicao[7][4]} | {posicao[7][5]} | {posicao[7][6]} | {posicao[7][7]} |
7 | {posicao[6][0]} | {posicao[6][1]} | {posicao[6][2]} | {posicao[6][3]} | {posicao[6][4]} | {posicao[6][5]} | {posicao[6][6]} | {posicao[6][7]} |
6 | {posicao[5][0]} | {posicao[5][1]} | {posicao[5][2]} | {posicao[5][3]} | {posicao[5][4]} | {posicao[5][5]} | {posicao[5][6]} | {posicao[5][7]} |
5 | {posicao[4][0]} | {posicao[4][1]} | {posicao[4][2]} | {posicao[4][3]} | {posicao[4][4]} | {posicao[4][5]} | {posicao[4][6]} | {posicao[4][7]} |
4 | {posicao[3][0]} | {posicao[3][1]} | {posicao[3][2]} | {posicao[3][3]} | {posicao[3][4]} | {posicao[3][5]} | {posicao[3][6]} | {posicao[3][7]} |
3 | {posicao[2][0]} | {posicao[2][1]} | {posicao[2][2]} | {posicao[2][3]} | {posicao[2][4]} | {posicao[2][5]} | {posicao[2][6]} | {posicao[2][7]} |
2 | {posicao[1][0]} | {posicao[1][1]} | {posicao[1][2]} | {posicao[1][3]} | {posicao[1][4]} | {posicao[1][5]} | {posicao[1][6]} | {posicao[1][7]} |
1 | {posicao[0][0]} | {posicao[0][1]} | {posicao[0][2]} | {posicao[0][3]} | {posicao[0][4]} | {posicao[0][5]} | {posicao[0][6]} | {posicao[0][7]} |
  | a | b | c | d | e | f | g | h |
"""

# class peca():
#     def __init__(self):
#         self.a = 1


a = [[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]]
#print(inter(a))


