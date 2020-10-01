''' Trabalho de Estrutura de Dados | Bruno Daniel Elias '''

from dados import Dados

class Fila:
    def __init__(self, limite):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        self.limite = limite
        
    def getInicio(self):
        return self.inicio
    
    def getFim(self):
        return self.fim
    
    def estaVazia(self):
        return self.tamanho == 0
    
    def estaCheia(self):
        return self.tamanho == self.limite
    
    def remove(self):
        if self.estaVazia() == True:
            raise Exception("Não há dados na fila!")
        else:
            if self.inicio == self.fim:
                self.inicio = None
                self.fim = None
                self.tamanho = 0
                return self.inicio
            else:
                self.fim = self.fim.getAnterior()
                self.tamanho -= 1
                return self.fim.getDado()

    def insere(self, dado:object):
        if isinstance(dado, Dados):
            if self.estaCheia() == False:
                if self.estaVazia() == True:
                    self.inicio = dado
                    self.fim = dado
                    self.tamanho = 1
                    return self.inicio.getDado()
                else:
                    dado.setAnterior(self.fim)
                    self.tamanho += 1
                    self.fim = dado
                    return self.fim.getDado()
            else:
                raise Exception("A fila está cheia!")
        else:
            raise Exception("O parâmetro passado é inválido")

dado1 = Dados(1)
dado2 = Dados(2)
fila = Fila(2)
fila.insere(dado1) # testa a inserção de dados na fila
fila.insere(dado2)
print(fila.estaCheia()) # testa se esta cheia - DEVE RETORNAR TRUE
print(fila.estaVazia()) # testa se esta vazia - DEVE RETORNAR FALSE
fila.remove()
print(fila.getInicio().getDado()) # o ultimo elemento foi removido corretamente
print(fila.estaCheia()) # deve retornar false
fila.remove()
print(fila.estaVazia()) # deve retornar um erro