# Usando AND: Uso da máscara e álcool
print("-"*40)
print("COMO ESTÁ O SEU USO DE MÁSCARA E ÁLCOOL?")
print("-"*40)
print()

uso_da_mascara = input("Você usa a máscara no rosto, cobrindo o nariz, e não no pescoço? [S/N] ")
uso_do_alcool = input("Usa álcool constantemente durante o dia? [S/N] ")
print()

if uso_da_mascara == "S" and uso_do_alcool == "S":
    print("Você não vai passar frio, pois está coberto de razão! Faça sempre a sua parte. <3\n")
elif uso_da_mascara == "N" and uso_do_alcool == "N":
    print("Opa, tem algo errado aqui! É preciso proteger a si e aos outros! :-(\n")
else:
    print("Parece que você não entendeu a pergunta... Que tal uma lida nos jornais? :-|\n")

print()


# Usando OR: Virando Jacaré
print("-"*49)
print("EM QUANTO TEMPO VOCÊ TOMA A VACINA E VIRA JACARÉ?")
print("-"*49)

print("1. Vai demorar de 3 a 5 dias\n")
print("2. Vai demorar de 1 a 2 anos\n")
print("3. Vai levar 6 anos\n")

resposta = int(input("Digite sua resposta: "))
print()

if resposta == 1 or resposta == 2 or resposta == 3:
    print("É bom já ir escolhendo o seu laguinho! \n")
else:
    print("Boa! Talvez só na outra encarnação! kkkkkkkkk :-D \n")

print()


# Usando NOT: Distanciamento Social
print("-"*55)
print("IMPORTÂNCIA DO DISTANCIAMENTO SOCIAL DURANTE A PANDEMIA")
print("-"*55)
print()

distanciamento = input("É preciso continuar controlando a disseminação do novo coronavírus! Responda: [S/N] ")
print()

if not distanciamento == "S":
    print("Que tal precisa pensar mais sobre o assunto?")
else:
    print("Você entendeu a importância do distanciamento!")

print()

