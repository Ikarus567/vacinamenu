class Elemento:
    def __init__(self,valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def inserir_inicio(self, valor):
        novo = Elemento(valor)              # cria um novo elemento
        novo.proximo = self.inicio    # o novo elemento ira aponta para o antigo início
        self.inicio = novo            # depois vai atualizar o inicio
        self.tamanho += 1            

    def inserir_fim(self, valor):
        novo = Elemento(valor)
        if self.inicio is None:          # caso a lista estiver vazia, o "novo" elemento vai se tornar o "início"
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo
    
    def remover_inicio(self):
        if self.inicio is None:
            return None 
        valor = self.inicio.valor     # guarda o "primeiro" elemento em valor  
        self.inicio = self.inicio.proximo # depois de "remover", o segundo vira o primeiro
        self.tamanho -= 1
        return valor  # devolve o elemento que foi tirado 

    def esta_vazia(self):

        return self.inicio is None
