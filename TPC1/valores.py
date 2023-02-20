class valores:
    def __init__(self,idade,sexo,tensao,colesterol,batimento,temDoenca) :
        self.idade = idade
        self.sexo = sexo
        self.tensao = tensao
        self.colesterol = colesterol
        self.batimento = batimento
        self.temDoenca = temDoenca

    def getIdade(self):
        return self.idade
    
    def getSexo(self):
        return self.sexo
    
    def getTensao(self):
        return self.tensao
    
    def getColesterol(self):
        return self.colesterol
    
    def getBatimento(self):
        return self.idade

    def getTemDoenca(self):
        return self.temDoenca

    def setIdade(self,idade):
        self.idade = idade
    
    def setSexo(self,sexo):
        self.sexo = sexo
    
    def setTensao(self,tensao):
        self.tensao = tensao
    
    def setColestero(self,colesterol):
        self.colesterol = colesterol

    def setBatimento(self,batimento):
        self.batimento = batimento

    def setTemDoenca(self,temDoenca):
        self.temDoenca = temDoenca

    def __str__(self):
        sep = ' | '
        res = str(self.idade)
        res += ' ' * (5-len(str(self.idade)))
        res += sep
        res += ' ' + self.sexo + '  '
        res += sep
        res += str(self.tensao)
        res += ' ' * (6-len(str(self.tensao)))
        res += sep
        res += str(self.colesterol)
        res += ' ' * (10-len(str(self.colesterol)))
        res += sep
        res += str(self.batimento)
        res += ' ' * (9-len(str(self.batimento)))
        res += sep
        res += str(self.temDoenca)
        res += ' ' * (9-len(str(self.temDoenca)))
        res += sep
        return res