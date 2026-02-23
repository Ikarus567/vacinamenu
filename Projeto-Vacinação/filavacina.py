from listaencadeada import ListaEncadeada

class Fila:
    def __init__(self):
        self.lista = ListaEncadeada()

    
    def enfileirar(self, valor): # Adiciona elemento no final da fila
        self.lista.inserir_fim(valor)

    def desenfileirar(self):
        return self.lista.remover_inicio()

    def esta_vazia(self):
        return self.lista.esta_vazia()

    def tamanho(self):
        return self.lista.tamanho

    def imprimir(self):
        atual = self.lista.inicio
        while atual:
            pessoa = atual.valor
            print(f"\nNome: {pessoa['nome']} | CPF: {pessoa['cpf']}")
            atual = atual.proximo
