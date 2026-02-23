class Elemento:
    def __init__(self,valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def inserir_inicio(self, valor):
        novo = Elemento(valor)              # Cria um novo elemento
        novo.proximo = self.inicio    # O novo elemento ira aponta para o antigo início
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
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo 
        self.tamanho -= 1
        return valor

    def esta_vazia(self):
        return self.inicio is None