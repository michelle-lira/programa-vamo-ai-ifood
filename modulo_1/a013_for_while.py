# # atividade pdf while
# fruta = str(input("Digite o nome de uma fruta: "))

# while fruta != "maçã":
#     tentativa = str(input("Tente novamente: ")).lower()
#     if tentativa == "maçã":
#         print("Você acertou!")
#         break


# atividade pdf while com função
def imprimeMultiplos(n1, n2):
    i = 1
    while i <= 10:
        print(n1 * i, n2 *i, "\t ")
        i = i + 1

imprimeMultiplos(7, 9)


# atividade pdf for 
# senhaBloqueio = "2468"

# for senhaBloqueio in range(2,10,2):
#   senhaBloqueio = input("digite sua senha: ")
#   if senhaBloqueio == "2468":
#     print("senha correta. acesso permitido")
#     break


# atividade pdf for com contador
# contador = 20

# for c in range(contador):
#     arquivo = "photoViagem{:04d}.jpg".format(c)
#     print(arquivo)
