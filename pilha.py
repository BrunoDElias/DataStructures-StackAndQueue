''' Trabalho de Estrutura de Dados | Bruno Daniel Elias '''

from dados import Dados

class Pilha:
    def __init__(self, limite):
        self.topo = None
        self.limite = limite
        
    def estaCheia(self):
        if self.topo == None:
            return False
        else:
            tamanho = 1
            dado = self.topo
            while dado.getAnterior() != None:
                dado = dado.getAnterior()
                tamanho += 1
            return tamanho == self.limite
        
    def estaVazia(self):
        return self.topo == None
    
    def getTopo(self):
        if self.estaVazia():
            raise Exception("A pilha está vazia!")
        else:
            return self.topo.getDado()
        
    def empilha(self, dado: object):
        if isinstance(dado, Dados) and self.estaCheia() == False:
            if self.estaVazia():
                self.topo = dado
                return dado.getDado()
            else:
                dado.setAnterior(self.topo)
                self.topo = dado
                return dado.getDado()
        else:
            raise Exception("Ops ocorreu um erro!")
        
    def desempilha(self):
        if self.estaVazia():
            raise Exception("A pilha ja está vazia!")
        else:
            dado = self.topo
            self.topo = dado.getAnterior()
            
dado1 = Dados(1)
dado2 = Dados(2)
dado3 = Dados(3)
p = Pilha(3)
p.empilha(dado1)
p.empilha(dado2)
p.empilha(dado3)
print(p.getTopo())
print(p.estaVazia()) #deve retornar false
print(p.estaCheia()) #deve retornar true
# p.empilha(dado3) deu erro entao ta certo
p.desempilha()
print(p.getTopo()) # funcionou
p.desempilha()
p.desempilha()
print(p.estaVazia()) #deve retornar true