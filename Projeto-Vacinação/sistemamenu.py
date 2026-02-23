from filavacina import Fila
from pilhavacina import Pilha

class SistemaVacinacao:
    def __init__(self):
        self.fila = Fila()
        self.pilha_frascos = Pilha()
        self.vacinados = []
        
        for i in range(3): # Empilha 3 frascos com 5 doses cada
            self.pilha_frascos.empilhar(5)
        self.doses_disponiveis = 15
        self.dose_atual = 0

    def adicionar_pessoa(self, nome, cpf):

        cpf = str(cpf)
        cpf = cpf.strip()
        cpf = cpf.replace(".", "").replace("-", "")

        if not cpf.isdigit():
            return "CPF inválido! Digite apenas números."

        if len(cpf) != 11:
            return "CPF deve conter exatamente 11 números."

        if self.fila.tamanho() >= 15:
            return "Fila cheia! Limite máximo de 15 pessoas."
        
        pessoa = {"nome": nome, "cpf": cpf}
        self.fila.enfileirar(pessoa)
        return "Pessoa adicionada com sucesso!"


    def vacinar_pessoa(self):    # Vacina a próxima pessoa da fila

        if self.fila.esta_vazia():
            return "Não há pessoas na fila."

        
        if self.doses_disponiveis == 0:   # Se as doses acabarem
            return "Não há mais doses disponíveis hoje."

        
        pessoa = self.fila.desenfileirar() # vai remover por ordem de chegada, ou seja FIFO
        self.dose_atual += 1
        self.doses_disponiveis -= 1
        self.vacinados.append(pessoa["nome"]) # guarda o nomes dos que ja foram vacinados

        mensagem = (
            f"\nPessoa vacinada!\n"
            f"Nome: {pessoa['nome']}\n"
            f"CPF: {pessoa['cpf']}\n"
            f"Dose aplicada hoje: {self.dose_atual}"
        )

        if self.dose_atual % 5 == 0:
            self.pilha_frascos.desempilhar()
            mensagem += "\nFrasco utilizado completamente!"
        return mensagem

    
    def imprimir_fila(self): # ira imprir as pessoas que ainda estão na fila
        if self.fila.esta_vazia():
            print("Fila vazia.")
        else:
            self.fila.imprimir()

    def total_vacinados(self):
        return len(self.vacinados)

    def doses_restantes(self):
        return self.doses_disponiveis
