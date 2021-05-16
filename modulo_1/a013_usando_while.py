# Exercitando aplicações do for e while

# numero = int(input("Digite um número: "))

# while numero != 50:
#    tentativa = int(input("Digite novamente: "))
#    if tentativa == numero:
#        print("Você acertou")
#    else:
#        print(tentativa)

# -----------------------------------------------------------

# for valor in range (1,4):
#     pedido = input("Quer namorar comigo? ").lower()
#     if pedido == "sim":
#         break
# print("Obrigado <3")

# -----------------------------------------------------------

# contador = 1

# while contador <= 5:
#     print("Olá, turma!")
#     contador = contador + 1

# -----------------------------------------------------------

numero = 1

while numero <= 10:
    multiplica = numero * 5
    print(multiplica)
    numero += 1

# -----------------------------------------------------------

# OUTROS EXEMPLOS WHILE:
# import math

# x = 1.0
# while x < 100.0:
#   print(x, '\t', math.log(x)/math.log(2.0))
#   x = x * 2.0

# -----------------------------------------------------------

# def sequencia(n):
#   while n != 1:
#     print(n)
#     if n%2 == 0:              # n é par
#       n = n/2
#     else:                     # n é impar
#       n = n*3+1

# sequencia(3)

# -----------------------------------------------------------

# def print_n(s, n):
#     if n <= 0:
#         return
#     print(s)
#     print_n(s, n-1)

# print_n("azul", 3)

# -----------------------------------------------------------

# def countdown(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)

# countdown(5)

