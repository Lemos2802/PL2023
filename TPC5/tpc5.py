import sys
import re
def validate_moedas(moedas):
        valid=[]
        invalid=[]
        for moeda in moedas:
            if moeda in ['1c','2c','5c','10c','20c','50c','1e','2e']:
                valid.append(moeda)
            else:
                invalid.append(moeda)
        return (valid,invalid)
def get_saldo_as_number(moedas):
        saldo=0
        for coin in [('1c',1),('2c',2),('5c',5),('10c',10),('20c',20),('50c',50),('1e',100),('2e',200)]:
            saldo+=moedas.count(coin[0])*coin[1]
        return saldo
    
    
class state:
    def __init__(self):
        self.saldo=0
        self.started=False
        
    def process_moedas(self,string):
        if self.started:
            string=string[6:-1]
            string=string.replace(' ','')
            validas,invalidas=validate_moedas(string.split(','))
            self.add_coins(validas)
            erradas=';'.join([ f"{c} - moeda inválida" for c in invalidas])
            if erradas!='': erradas+=';'
            print(erradas+f" saldo = {self.get_saldo()}")
        else:
            print("pega no telefone primeiro")    
    
    def add_coins(self,moedas):
        self.saldo=get_saldo_as_number(moedas)
         
    def get_saldo(self):
        return f"{self.saldo//100}e{self.saldo%100}c"
    
    def process_telefone(self,string):
        if self.started:
            cobrar=0
            string=string[2:]
            if string.startswith('601') or string.startswith('641'):
                print("Esse número não é permitido neste telefone. Queira discar novo número!")
                return
            elif string.startswith('00'):
                cobrar=150
            elif string.startswith('2'):
                cobrar=25
            elif string.startswith('800'):
                cobrar=0
            elif string.startswith('808'):
                cobrar=10
            else:
                print('O numero n existe')
                return
            if cobrar>self.saldo:
                print("Saldo insuficiente")
            else:
                self.saldo-=cobrar
                print(f"Saldo = {self.get_saldo()}")
        else:
            print("pega no telemovel")
    def troco(self):
        saldoL=self.saldo
        s=[]
        for coin in [('2e',200),('1e',100),('50c',50),('20c',20),('10c',10),('5c',5),('2c',2),('1c',1)]:
            c = saldoL//coin[1]
            if c>0:
                saldoL=saldoL%coin[1]
                s.append(f"{c}x{coin[0]}")
        return ', '.join(s)
        
    def mainLoop(self):
        for line in sys.stdin:
            line=line[:-1]
            if line.startswith('T='):
                self.process_telefone(line)
            elif line.startswith('MOEDA'):
                self.process_moedas(line)
            elif line=='LEVANTAR':
                self.started=True
                self.saldo=0
                print("Introduza moedas.")
            elif line=='POUSAR' or line=='ABORTAR':
                self.started=False
                print("troco= "+self.troco())
            else:
                print("linha invalida")
        
                
c=state()
c.mainLoop()