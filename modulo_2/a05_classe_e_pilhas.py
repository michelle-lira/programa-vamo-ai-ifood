class Pilha:
    def __init__(self):
        self.stack = []

    
    def push(self, item):
        self.stack.append(item)


    def pop(self):
        if self.tamanho == 0:
            return None
        else:
            return self.stack.pop()


    def tamanho(self):
        return len(self.stack)


Roupas = Pilha()
print(Roupas.stack)

Roupas.tamanho()
print(Roupas.stack)

Roupas.push("Short")
print(Roupas.stack)

Roupas.push("Blusa com alças")
print(Roupas.stack)

Roupas.push("Vestido longo")
print(Roupas.stack)

Roupas.push("Calça jeans")
print(Roupas.stack)

Roupas.push("Casaco de linha")
print(Roupas.stack)

Roupas.pop()
print(Roupas.stack)

Roupas.tamanho()
print(Roupas.stack)

