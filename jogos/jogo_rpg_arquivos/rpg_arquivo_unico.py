# jogo de rpg no python

# import random
from random import*
from time import*

RESET = "\033[0m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
CINZA = '\033[90m'
ROXO = '\033[35m'

class Classe():  # usado para definir atributos para as classes de jogadores 
    classes = ['guerreiro', 'mago', 'atirador']
    def __init__(self,nome):
        self.nome_clas = nome
        self.ataque_especial = ''
        self.dano_especial = 0
        self.classe_atrib()
    
    def classe_atrib(self):
        match self.nome_clas:
            case 'guerreiro':
                self.ataque_especial = 'corte pesado' # determina o nome do ataque especial
                
            case 'mago':
                self.ataque_especial = 'bola de fogo'

            case 'atirador':
                self.ataque_especial = 'tiros multiplos'
        
# caso o sistema não funcione com o match case esta aqui a parte com o if,elif

        """if self.nome_clas == 'guerreiro':
            self.ataque_especial = 'corte pesado' # determina o nome do ataque especial
            
        elif self.nome_clas == 'mago':
            self.ataque_especial = 'bola de fogo'

        elif self.nome_clas == 'atirador':
            self.ataque_especial = 'tiros multiplos'"""


        dano_especial = randrange(5,30,5) # determina um dano para o ataque especial 
        self.dano_especial = dano_especial

class Jogador(): # usado para criar um jogador
    racas = ['humano', 'elfo', 'anão']
    def __init__(self,classe='', raca=''):
        self.classe = Classe(classe)
        self.raca = raca
        self.arma = Arma(classe)
        self.hp = 0
        self.dano_base = 0
        self.raca_jogador()
        self.hp_max = self.hp # sertve para ver o valor maximo de vida como 100/100 e para restalrar o hp maximo

    def raca_jogador(self): # usdo para adicionar os atrinutos
        match self.raca :
            case 'humano':
                self.hp = 150
                self.dano_base = 20

            case 'elfo':
                self.hp = 200
                self.dano_base = 10
                
            case 'anão':
                self.hp = 100
                self.dano_base = 30
# caso o sistema não funcione com o match case esta aqui a parte com o if,elif
        """if self.raca == 'humano':
            self.hp = 150
            self.dano_base = 20
        elif self.raca == 'elfo':
            self.hp = 200
            self.dano_base = 10
        elif self.raca == 'anão':
            self.hp = 100
            self.dano_base = 30"""

    def atacar(self, monstro, tipo_ataque): # metodo que serve para atacar 
        # o ataque "1" nao esiste por que é a escolha de fugir
        if tipo_ataque == '2': # se o ataque for "2" , que é um ataque com as mãos, vai ser somente um dano basico
            monstro.hp = monstro.hp - self.dano_base
            print(f'\ndano causado ao {monstro.raca}: {self.dano_base}')

        elif tipo_ataque == '3': # se o ataque for "3" , que é um ataque com a arma , vai ser um ataque com as mãos mais o da arma 
            if self.arma.durab <= 0: # se a arma estiver quebrada nao sera posivel usar o golpe 
                print('arma está quebrada não tem como usa-la ')
                monstro.hp = monstro.hp - self.dano_base
                print(f'\ndano basico causado ao {monstro.raca}: {self.dano_base}')
            
            else: # se a arma estiver utilizavel sera posivel atacar
                dano_total = self.dano_base + self.arma.dano 
                monstro.hp = monstro.hp - dano_total
                self.arma.durab -= self.arma.durab_retidada 
                print(f'\ndano causado ao {monstro.raca}: {dano_total}')

        elif tipo_ataque == '4': # se o ataque for "4" , que é um ataque especial com a arma , vai ser um ataque com as mãos mais o da arma mais o especial
            if self.arma.durab <= 0:  # se a arma estiver quebrada nao sera posivel usar o golpe 
                print('arma está quebrada')
                monstro.hp = monstro.hp - self.dano_base
                print(f'dano causado ao {monstro.raca}: {self.dano_base}')
            
            else:  # se a arma estiver utilizavel sera posivel atacar
                dano_total = self.dano_base + self.arma.dano + self.classe.dano_especial
                monstro.hp = monstro.hp - dano_total
                self.arma.durab -= self.arma.durab_retidada 
                print(f'\ndano causado ao {monstro.raca}: {dano_total}')

class Monstro(): # usado para criar um monstro
    def __init__(self):
        self.raca = ''
        self.tipo = ''
        self.hp = 0
        self.dano_base = 0
        self.probab_tipo = []
        self.raca_monstro()
        self.tipo_monstro()
        while self.tipo == '':
            self.tipo_monstro()
        self.hp_max = self.hp

    def raca_monstro(self): # dependendo do monstro ele tem atributo diferente
        racas = ['lobo','goblin','slime']
        self.raca = choice(racas) # escolhe a raca monstro aleatoriamente
        match self.raca:
            case 'slime':
                self.hp = 5
                self.dano_base = 5
            case 'lobo':
                self.hp = 25
                self.dano_base = 10
            case 'goblin':
                self.hp = 50
                self.dano_base = 15
# caso o sistema não funcione com o match case esta aqui a parte com o if,elif
        """if self.raca == 'slime':
            self.hp = 5
            self.dano_base = 5
        elif self.raca == 'lobo':
            self.hp = 25
            self.dano_base = 10
        elif self.raca == 'goblin':
            self.hp = 50
            self.dano_base = 15
"""


    def tipo_monstro(self): # mesma coisa com a raca
        # o "tipo" basico se reéte maispara nao surgir boses ou titãns toda hora
        
        lista_tipos = ['basico', 'titãn', 'boss'] 
        probab_tipos = []
        probabilidade(lista_tipos, probab_tipos)
        self.probab_tipo = probab_tipos
        probab = randrange(1,100)

        if probab <= self.probab_tipo[0]:
            self.tipo = 'basico'

        elif probab > self.probab_tipo[0] and probab <= self.probab_tipo[1]:
            self.tipo = 'titãn'
            self.hp += 100
            self.dano_base += 15

        elif probab > self.probab_tipo[1] and probab <= self.probab_tipo[2]:
            self.tipo = 'boss'
            self.hp += 150
            self.dano_base += 25
        
        else:
            pass
                
    def atacar(self,jogador):
        jogador.hp = jogador.hp - self.dano_base
        print(f'\ndano causado ao {jogador.raca}: {self.dano_base}')

class Arma(): # usado para criar e definir atributos a uma arma
    def __init__(self, classe):
        self.classe_jogador = classe
        self.tipo = ''
        self.dano = 0
        self.durab = 0
        self.durab_retidada = 0
        self.rarid_cor = ''
        self.raridade_arma = ''
        self.probab_raridade = []
        self.tipo_arma()
        self.buf_raridade()
        while self.raridade_arma == '':
            self.buf_raridade()
        self.durab_max = self.durab
        
    def tipo_arma(self): 

        match self.classe_jogador: 
            case 'guerreiro':
                tipos = ['machado', 'espada', 'espada longa']
                self.tipo = choice(tipos) 
                
               
            case 'mago':
                tipos = ['varinha', 'crajado', 'grimorio']
                self.tipo = choice(tipos)

            case 'atirador':
                tipos = ['arco', 'besta', 'pistola']
                self.tipo = choice(tipos)

# caso o sistema não funcione com o match case esta aqui a parte com o if,elif

        """if self.classe_jogador == 'guerreiro':
                tipos = ['machado', 'espada', 'espada longa']
                self.tipo = choice(tipos)

        elif self.classe_jogador =='mago':
                tipos = ['varinha', 'crajado', 'grimorio']
                self.tipo = choice(tipos)

        elif self.classe_jogador =='atirador':
                tipos = ['arco', 'besta', 'pistola']
                self.tipo = choice(tipos)"""
        


       # raridade : comum , incomun , raro , lendario , mitico
       # serve para reduzir a posibilidade de vir armas raras
        lista_raridade = ['comum', 'incomum', 'rara', 'epica', 'lendaria', 'mitica'] #lista com cada raridade 
        probab_raridade = [] # lista para guardar a probabilidade das raridade
        probabilidade(lista_raridade, probab_raridade) 
        self.probab_raridade = probab_raridade

    def buf_raridade(self): #sistema para criar buff de acordo com a raridade do obj
        raridade = randrange(1,100)
        #print(f'raridade {raridade}') ########################################
        #print(f'probab_raridade {probab_raridade}') ########################################

        if raridade <= self.probab_raridade[0]:
            self.rarid_cor = CINZA
            self.raridade_arma = f'{CINZA}comum{RESET}'
            self.dano = randrange(5,15,5) # quantidade de dano da arma
            self.durab = randrange(50,150,5) # limita a quantidade de ataques que um jogador pode calsar com a arma 
            self.durab_retidada = 25 # determina quanto de durabilidade é retirada a cada golpe feito 
            

        elif raridade > self.probab_raridade[0] and raridade <= self.probab_raridade[1]:
            self.rarid_cor = VERDE
            self.raridade_arma = f'{VERDE}incomum{RESET}'
            self.dano = randrange(15,25,5) 
            self.durab = randrange(150,250,5) 
            self.durab_retirada = 20
            

        elif raridade > self.probab_raridade[1] and raridade <= self.probab_raridade[2]:
            self.rarid_cor = AZUL
            self.raridade_arma = f'{AZUL}raro{RESET}'
            self.dano = randrange(25,35,5) 
            self.durab = randrange(250,350,5) 
            self.durab_retirada = 15
            

        elif raridade > self.probab_raridade[2] and raridade <= self.probab_raridade[3]:
            self.rarid_cor = ROXO
            self.raridade_arma = f'{ROXO}epico{RESET}'
            self.dano = randrange(35,45,5) 
            self.durab = randrange(350,450,5) 
            self.durab_retirada = 10
            

        elif raridade > self.probab_raridade[3] and raridade <= self.probab_raridade[4]:
            self.rarid_cor = AMARELO
            self.raridade_arma = f'{AMARELO}lendario{RESET}'
            self.dano = randrange(45,55,5) 
            self.durab = randrange(450,550,5) 
            self.durab_retirada = 5
            
        
        else :
            pass

def probabilidade(sistema, probab): #sistema para criar a probabilidade
    for i in range(len(sistema)): #sistema para criar a porcentagem
        
        if i == 0: 
            probab.append(100 / 2)

        else:
            probab.append(probab[i-1] / 2)
        
        #print(f'probab {probab}') ########################################
        
    for i in range(len(probab)): # sistema para criar a probabilidade de surgir algum valor
        #print(f'probab {probab}') ########################################
        if i == 0: pass

        else:
            probab[i] = (probab[i-1] + probab[i])

def status(entidade,tipo): # serve para mostrar os atributos do jogador ou do monstro
    if tipo == 'batalha': # mostra somente dados importantes em batalha
        print(entidade.raca)
        print(f'hp: {entidade.hp}/{entidade.hp_max}')
        try: # se nao ouver arma nao mostra durabilidade
            print(f'durabilidade da arma: {entidade.arma.durab}/{entidade.arma.durab_max}')
        
        except AttributeError:
            pass
    
    elif tipo == 'fixa': # mostra todos os dados da entidade 
        print('raça: ', entidade.raca) 
        try: # se nao ouver classe como os monstros acaba substituindo por tipo
            print('classe: ', entidade.classe.nome_clas)
        except AttributeError:
            print('tipo: ', entidade.tipo)
        
        print(f'hp: {entidade.hp}/{entidade.hp_max}')
        print('dano base: ', entidade.dano_base)

        try: #  se nao ouver arma nao sera mostrado nd
            print('ataque especial: ', entidade.classe.ataque_especial)
            print('dano especial: ', entidade.classe.dano_especial)
            print(f'arma: {entidade.arma.rarid_cor}{entidade.arma.tipo}{RESET}')
            print('dano da arma: ', entidade.arma.dano)
            print(f'durabilidade da arma {entidade.arma.durab}/{entidade.arma.durab_max}')
            print(f'raridade da arma: {entidade.arma.raridade_arma}')
        except AttributeError:
            pass

def batalha(jogador): # serve para criar as batalhas 
    contador = 0 # mostra quantas lutas em seguida o jogador lutou 
    while True:
        monstro1 = Monstro() # criaçao de um montro para o jogo

        if jogador.hp > 0 : # se o jogador estiver vivo ele tera direito a escolher entre fugir de uma luta ou lutar
            print(f'\n{jogador.raca} encontra {monstro1.raca} do tipo {monstro1.tipo}')
            escolha = input(f'{jogador.raca} escolhe: \n1)fugir\n2)lutar\n==> ')
            
            if escolha in ['1', 'fugir']: # escolha 1, se o jogador decidir fugir da luta ele acaba tendo tres escolhas sair da floresta, continuar na floresta, ou acampar
                print(f'\nO {jogador.raca} foge para longe\n')
                opcao = input('Você decide continuar na floresta, sair ou acampar\n1)continuar\n2)sair\n3)acampar\n==>')
                
                # escolha 1.1, se o jogador escolher continuar ele nao regenera hp e continua a aparecer monstros

                if opcao in ['2','sair']: # escolha 1.2, se jogador decidir sair ele recupera seu hp e nao luta mais anao ser que volte
                    jogador.hp = jogador.hp_max
                    espera(2,'Saindo')
                    print(f'{jogador.raca} sai da floresta')
                    break

                elif opcao in ['3','acampar']: #escolha 1.3, se jogador acampar ele regenera o hp e depois volta para a luta
                    jogador.hp = jogador.hp_max
                    espera(5,'Acampando')
                    print(f'{jogador.raca} acampa na floresta')

                while opcao not in ['1', 'continuar','2','sair','3','acampar']: # sistema de indentificação de erro , caso nao seja escolido nada que esteja no sistema aparece uma mensagem 
                    print('Opção inesistente')
                    opcao = input('Você decide continuar na floresta, sair ou acampar\n1)continuar\n2)sair\n3)acampar\n==>')
            
            elif escolha in ['2','atacar']: # escolha 2, se decidir atacar vai aparecer os status de batalha de cada jogador 
                status(monstro1,'batalha')
                status(jogador,'batalha')
                
                while True : # "area de batalha"
                    
                    if jogador.hp <= 0: # se jogador morrer acaba a luta 
                        print(f'\nFim da batalha contra {monstro1.raca}')
                        break
                        
                    elif monstro1.hp <= 0: # se monstro morrer a luta acaba e mostra que ele morreu
                        print(f'\nFim da batalha contra {monstro1.raca}')
                        print(f'{monstro1.raca} morreu')
                        break

                    if contador >= 1 : # o jogador so pode usar o especial apos 5 batalhas 
                        #jogador recebe a escolha de fugir , atacar , atacar com sua arma ou usar o especial
                        escolha = input(f'\n{jogador.raca} escolhe: \n1)fugir\n2)atacar com a mão\n3)atacar com {jogador.arma.tipo}\n4)ataque especial {jogador.classe.ataque_especial}\n==> ')
                    
                    else:
                        #jogador recebe a escolha de fugir , atacar , atacar com sua arma ou usar o especial
                        escolha = input(f'\n{jogador.raca} escolhe: \n1)fugir\n2)atacar com a mão\n3)atacar com {jogador.arma.tipo}\n4)ataque especial incompleto {contador}/1 batalhas concluidas\n==> ')

                    if escolha == '1': #escolha 2.1, se jogador escolher fugir ele só foge da batalha 
                        print(f'O {jogador.raca} foge')
                        break
                    
                    # escolha 2.2 , 2.3 e 2.4, aqui é determinado qual o ataque e quanto de dano sera causado
                    jogador.atacar(monstro1, escolha ) # a escolha determina qual o ataque, o ataque é decidido na classe jogador
                    status(monstro1,'batalha')
                    if escolha == "4":
                        contador -= 2
                    if monstro1.hp > 0:
                        monstro1.atacar(jogador)
                        status(jogador,'batalha')
                    if contador <= 0:
                        contador += 1 # contador para saber quantas lutas o jogador ja teve
                
                else:
                    pass

                

            else: # validação de erro 
                print('opcao invalida')
                match monstro1.tipo:
                    case 'basico':
                        print(f'{monstro1.raca} foge pensando ser um ataque poderso')
                    case _:
                        print(f'{monstro1.raca} pensa que {jogador1.raca} paralisou de medo e sai com pena')
                
# caso o sistema não funcione com o match case esta aqui a parte com o if,elif
                """ if  monstro1.tipo =='basico':
                    print(f'{monstro1.raca} foge pensando ser um ataque poderso')
                    
                else:
                    print(f'{monstro1.raca} pensa que {jogador1.raca} paralisou de medo e sai com pena')"""
                    
        else: # se jogador morrer aparece essa mensagem
            print(f'{jogador.raca} morreu')
            break

def espera(repetir=2, mensagem = 'Carregando'): # serve para mostrar os pontinhos em sistemas de loading
    for i in range(repetir):
        print(f'{mensagem} .  ', sep=sleep(0.3), end='\r') 
        print(f'{mensagem} .. ', sep=sleep(0.3), end='\r')
        print(f'{mensagem} ...', sep=sleep(0.3), end='\r')
    print('    ',+len(mensagem)*' ' ,end='\r') # serve para limpar os pontos e a mensagen

while True: #jogatina
    # escolher classe
    print('\nEscolha uma classe:')
    for classe in Classe.classes:
        print(classe)

    classe = input('==> ').lower()
    while classe not in Classe.classes:
        classe = input('Classe inesistente\nTente novamente\nescolha uma classe:\n==> ').lower()

    # escolher raca 
    print('\nEscolha uma raça:')
    for raca in  Jogador.racas:
        print(raca)

    raca = input('==> ')
    while raca not in Jogador.racas:
        raca = input('Raça inesistente\nTente novamente\nescolha uma raça:\n==> ').lower()
    
    # criação da fixa
    espera(3, 'Criando fixa')
    print('\n')
    jogador1 = Jogador(classe, raca) # criar jogador
    status(jogador1,'fixa')  #mostrar um jogador


    escolha = input(f'\n{jogador1.raca} deseja:\n1)ir a floresta\n2)sair\n==> ')
    while jogador1.hp > 0 or escolha not in ['2','sair'] : 
        batalha(jogador1)
        if jogador1.hp <= 0:
            print('E assim morre mais um aventureiro')
            escolha = input(f'\nVocê deseja:\n1)renascer\n2)sair\n==> ')
            while escolha not in ['1','renascer','2','sair']:
                print('Não há outra escolha ')
                escolha = input(f'\nVocê deseja:\n1)renascer\n2)sair\n==> ')
            break

        escolha = input(f'\n{jogador1.raca} deseja:\n1)voltar a floresta\n2)sair\n==> ')

    if escolha in ['2','sair']:
        espera(3,'Saindo')
        break