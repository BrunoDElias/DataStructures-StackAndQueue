''' Trabalho de Estrutura de Dados | Bruno Daniel Elias '''

class Dados:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        
    def getDado(self):
        return self.dado
    
    def getAnterior(self):
        return self.anterior
    
    def setAnterior(self, dado):
        self.anterior = dado
