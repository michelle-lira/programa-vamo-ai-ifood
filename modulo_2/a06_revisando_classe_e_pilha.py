# REVISANDO: Classes e Pilhas

# def autentica(self, senha):
#     if self._senha == senha:
#         print("acesso permitido")
#         return True
#     else:
#         print("acesso negado")
#         return False


# ----------------------------------------------------

# Exemplo de classe sem o __init__:

# class Pizza:
#     pedacos = 8

# ----------------------------------------------------
#     def altera_tamanho(self, pedacos):
#         self.pedacos = pedacos

# 

# ---------------------------------------------------
# ATIV BREAKOUT AULA 6: CRIAR UMA PILHA (REVISANDO)
class Pilha:
    def __init__(self):
        self.stack = []


    def tamanho(self):
        return len(self.stack)


    def incluir(self, carta):
        self.stack.append(carta)


    def excluir(self):
        if self.tamanho() == 0:
            return None
        else:
            return self.stack.pop()


Baralho = Pilha()

Baralho.incluir("Rainha de Copas")
print(Baralho.stack)

Baralho.incluir("Rainha de Ouros")
print(Baralho.stack)

Baralho.incluir("Rainha de Espadas")
Baralho.incluir("Rainha de Paus")
print(Baralho.stack)


Baralho.tamanho()
print(Baralho.stack)

Baralho.excluir()
print(Baralho.stack)

Baralho.excluir()
print(Baralho.stack)

# SAÍDA NO TERMINAL
'''
['Rainha de Copas']
['Rainha de Copas', 'Rainha de Ouros']
['Rainha de Copas', 'Rainha de Ouros', 'Rainha de Espadas', 'Rainha de Paus']
['Rainha de Copas', 'Rainha de Ouros', 'Rainha de Espadas', 'Rainha de Paus']
['Rainha de Copas', 'Rainha de Ouros', 'Rainha de Espadas']
['Rainha de Copas', 'Rainha de Ouros']
'''

