class Fila:
    def __init__(self):
        self.queue = []

    
    def partida(self):
        if self.tamanho() == 0:
            return None
        else:
            return self.queue.pop(0)


    def chegada(self, item):
        self.queue.append(item)


    def tamanho(self):
        return len(self.queue)


Musicas = Fila()
# print(Musicas.queue)

Musicas.tamanho()
print(Musicas.queue)

Musicas.chegada("The House of The Rising Sun")
print(Musicas.queue)

Musicas.chegada("The Sound of Silence")
print(Musicas.queue)

Musicas.chegada("Unchained Melody")
print(Musicas.queue)

Musicas.chegada("Yesterday")
print(Musicas.queue)

Musicas.partida()
print(Musicas.queue)

Musicas.chegada("Good Morning")
print(Musicas.queue)

Musicas.partida()
print(Musicas.queue)

Musicas.partida()
print(Musicas.queue)
