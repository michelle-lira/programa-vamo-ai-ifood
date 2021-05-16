# Calcular média com if e else
nota_matematica_1 = float(input("Digite a primeira nota: "))
nota_matematica_2 = float(input("Digite a segunda nota: "))
nota_matematica_3 = float(input("Digite a terceira nota: "))

media_matematica = (nota_matematica_1 + nota_matematica_2 + nota_matematica_3) / 3

# Condição
if media_matematica < 6:
    print("Você precisa estudar mais. Ainda não foi aprovado. :-( ")
else:
    print("Parabéns. Você foi aprovado! :-) ")
