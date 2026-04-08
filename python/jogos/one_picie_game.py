# # jogo de texto do one picie
# Elementos do jogo:
# - baús do tesouro com chance baixa de apareceu uma akumanomi
# - para aparecer uma akumanomi precisa ter a chance de aparecer uma fruta em um baú ou o baú pode já ter uma akumanomi
# - os baús precisam ter moedas 
# - sistema de combate contra marinha ou contra piratas , e de vez emquanto contra animais 
# - sistema de compra de navios 
# - talvez tenha como contratar companheiros 
# - ...
# Yuki Yuki no mi , hebi hebi no mi, soru soru no mi , fude fude no mi , ou ou no mi
import random as rd
# este dicionario é feito para ver se a akuma no mi ja foi coletada ou nao 
akuma_no_mis_dict = {"Yuki Yuki no mi" : False, 'hebi hebi no mi modelo yamata no horoti' : False,'ou ou no mi' : False}


class Akuma_no_mi():
    def __init__(self, nome = "não akumado"):
        self.nome = nome
        self.tipo = 'nenhum'
        self.ataques = "nenhuma"
        self.dano = 0
        self.hp_estra = 0
        self.descricao = "nenhuma"
        self.valor = 0
        self.atributos
    
    def atributos(self):
        akuma_no_mis_dict_atribultos = {'nome':"Yuki Yuki no mi" , 'atributos' : '', 'nome':'hebi hebi no mi modelo yamata no horoti' , 'nome':'ou ou no mi'}
        if self.nome == "Yuki Yuki no mi":
            ...
        
        elif self.nome == 'hebi hebi no mi modelo yamata no horoti':
            ...
        
        elif self.nome == 'ou ou no mi':
            ...

class Player():
    def __init__ (self, nome, idade, raca, tipo, profissao ):
        # caracteristicas do personagem
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.tipo = tipo
        self.profissao = profissao
        self.akuma_no_mi = "nenhuma "
        self.haki = 'Haki()'
        # dados de jogo
        self.hp = rd.randrange(100,300,5)
        self.dano = rd.randrange(5,40,5)
        self.berie = 0
        self.iventario_akumanomi = ['nenhuma']
         
    def comer_akumanomi(self):
        if len(self.iventario_akumanomi) < 1:
            for i,fruta in enumerate(self.iventario_akumanomi()):
                print(i,')',fruta)
            escolha_akuma_no_mi = input("escolha uma akuma no mi do inventario para comer")
            escolha_descisao = input('Deseja mesmo comer a ', self.iventario_akumanomi[escolha_akuma_no_mi],'\n1)Sim\n2)Não\n==>').lower()
            if escolha_descisao in ['s','sim','1']:
                self.akuma_no_mi = Akuma_no_mi(self.iventario_akumanomi[escolha_akuma_no_mi])
                self.hp += self.akuma_no_mi.hp_estra
                self.dano += self.akuma_no_mi.dano
        
        elif len(self.iventario_akumanomi) == 1:
            print('Há só uma akuma no mi no inventario ')
            escolha_descisao = input('Deseja mesmo comer a ', self.iventario_akumanomi[0],'\n1)Sim\n2)Não\n==>').lower()
            if escolha_descisao in ['s','sim','1']:
                self.akuma_no_mi = Akuma_no_mi(self.iventario_akumanomi[escolha_akuma_no_mi])
                self.hp += self.akuma_no_mi.hp_estra
                self.dano += self.akuma_no_mi.dano
        
        else: print('Não há akuma no mi no seu inventario ')



    def dados(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nRaça: {self.raca}\nTipo: {self.tipo}\nProfissão: {self.profissao}\nAkuma no Mi: {self.akuma_no_mi}\nHP: {self.hp}\nDano: {self.dano}'

class Bau():
    def __init__(self):
        self.armas = []
        self.itens = []
        self.akuma_no_mi = ''
        self.criar_akuma_no_mi()
        self.criar_item()
    
    def criar_akuma_no_mi(self):
        akuma_no_mi_list = ["Yuki Yuki no mi" , 'hebi hebi no mi modelo yamata no horoti' ,'ou ou no mi' ]
        akuma_no_mi = rd.choice(akuma_no_mi_list)

        if akuma_no_mis_dict["Yuki Yuki no mi"] != True or akuma_no_mis_dict['hebi hebi no mi modelo yamata no horoti'] != True or akuma_no_mis_dict['ou ou no mi'] != True:
            while akuma_no_mis_dict[akuma_no_mi] == True:
                akuma_no_mi = rd.choice(akuma_no_mi_list)
        else:
            akuma_no_mi = ''
        self.akuma_no_mi = akuma_no_mi
        akuma_no_mis_dict[akuma_no_mi] = True
    

    def criar_item(self):
        item_list = [{'item':'taça de ouro','valor':'10000'},{'item':'moeda de ouro','valor':'2000'},{'item':'colar','valor':'44000'},{'item':'coroa de ouro','valor':'100000'}]
        quant_intens = rd.randint(3,10)
        for i in range(quant_intens):
            self.itens.append(rd.choice(item_list))


import time as tm
while True:
    bau=Bau()
    print(bau.akuma_no_mi)
    for i in bau.itens:
        print(i['item'])
        tm.sleep(2)

    tm.sleep(2)
