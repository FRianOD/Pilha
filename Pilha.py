class Dado:
    def __init__(self,valor):
        self.valor = valor
        self.prox = None

class Pilha:
    def __init__(self):
        self.topo = None
        self.numeroDeElementos = 0
        
    def estaVazia(self):
        if self.topo is None: return True 
        else: return False
        
    def empilhar(self, valor):
        
        novoDado = Dado(valor)
        
        if self.estaVazia():
            self.topo = novoDado
        else: 
            novoDado.prox = self.topo
            self.topo = novoDado
            
        self.numeroDeElementos += 1
        
    def desempilhar(self):
        
        if self.estaVazia(): return f"pilha vazia"
        
        lixo = self.topo
        self.topo = self.topo.prox
        self.numeroDeElementos -= 1
        return lixo.valor

    def tamanho(self):
        return self.numeroDeElementos
    
    def buscar(self, valor):
        
        if self.estaVazia(): return "pilha vazia"
        
        temp = self.topo
        
        while temp != None:
            if temp.valor == valor:
                return f"O valor {temp.valor} esta na pilha"
            temp = temp.prox
        else: return f"O valor {valor} não esta na pilha !!"
        
    def mostrarPilha(self):
        
        if self.estaVazia(): return "pilha vazia"
        
        temp = self.topo
        
        print("[", end="")
        while temp.prox != None:
            print(f"{temp.valor}", end=", ")
            temp = temp.prox
        else:
            print(f"{temp.valor}]")