# Exemplo Aula
# lista_de_compras = ["cerveja", "miojo", "pão", "pão de alho", "carne", "açaí"]
# print(lista_de_compras)

# lista_valores = [5, 19, 32, "Turma VamoAI", 73, 84, 99]
# print(lista_valores)

# ------------------------------------------------------------------
# Exercício Breakout: Fazer lista e testar -> append, pop, remove, count, reverse, insert, len, lista com repartição

fruta = ("Morango")
legume = "batata"
carne = "peixe"
raiz = "batata-doce"
lanche = "pão de queijo"
queijo = "mussarela"
bebida = "água"

comida = [fruta, legume, carne, raiz, lanche, queijo, bebida]

# Adiciona elemento
comida.append("lasanha")
print(comida)

# Remove elemento indicado pela posição
comida.pop(1)
print(comida)

# Remove elemento indicado na lista
comida.remove(bebida)
print(comida)

# Exibe a quantidade de ocorrências de um elemento na lista
comida.count(bebida)
print(comida)

# Exibe comprimento da lista
len(comida)
print(comida)

# Exibe a lista na ordem inversa
comida.reverse()
print(comida)

# Insere elemento em determinada posição 
comida.insert(0, "caju")
print(comida)

# Exibe parte da lista de acordo com a posição do elemento
print(comida[::3])
print(comida)

# Insere elemento na lista de acordo com a posição informada
comida.insert(1, "10")
print(comida)

# Ordena a lista
comida.sort()
print(comida)

comida.sort()
print(comida)

# --------------------------------------------------------
# Exemplo: Gi
# fruta1 = input("Digite as frutas que deseja: ")
# # fruta2 = input("Digite a fruta que deseja: ")
# # fruta3 = input("Digite a fruta que deseja: ")

# frutas = [fruta1]
# print(frutas)

# pode fazer assim
# num = []
# for c in range(0,3):
#     num.append (int(input('Digite um numero: ')))
# print(num)

