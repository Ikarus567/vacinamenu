from listaencadeada import ListaEncadeada

class Pilha:
    def __init__(self):
        self.lista = ListaEncadeada()

    def empilhar(self, valor): # Adiciona elemento no topo da pilha
        self.lista.inserir_inicio(valor)

    def desempilhar(self): # Remove elemento do topo da pilha
        return self.lista.remover_inicio()

    def esta_vazia(self):     # Verifica se a pilha está vazi
        return self.lista.esta_vazia()

    def tamanho(self): # Retorna quantidade de elementos na pilha
        return self.lista.tamanho
