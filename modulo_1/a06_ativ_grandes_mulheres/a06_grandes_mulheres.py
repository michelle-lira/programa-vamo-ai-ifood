# Mulheres Stem
print()
print("★  "*12)
print(" MULHERES STEM, MULHERES INCRÍVEIS")
print("★  "*12)
print()

print("VAMOS DESCOBRIR O QUE VOCÊ SABE SOBRE: \n", "~ "*5, " BERTHA LUTZ! ", "~ "*5)

# O que ela foi
print("\n1. Qual a formação acadêmica de Bertha Lutz?")

print("\na) Ciências, na Sorbonne \nb) Medicina, em Cambridge \nc) Ciência Política, em Oxford")
pergunta1 = input("Resposta: ")
print()

# Onde nasceu
print("\n2. Em qual país ela nasceu?")

print("\na) Hungria \nb) França \nc) Brasil")
pergunta2 = input("Resposta: ")
print()

# Ganhou popularidade por atuar com:
print("\n3. Dedicou-se por várias décadas a(o): ")

print("\na) Aprimoramento de técnicas de criptografia \nb) Defesa do sufrágio feminino \nc) Cura do câncer")
pergunta3 = input("Resposta: ")

acertos = 0
plural = "resposta"

if pergunta1 == "a":
    acertos +=  1
if pergunta2 == "c":
    acertos += 1
if pergunta3 == "b":
    acertos += 1

if acertos == 1:
    plural = "respostas"

if acertos == 0:
    print(f"\nQue pena, você não acertou nenhuma resposta. Tente novamente!")
else:
    print(f"\nVocê acertou {acertos} {plural}! Leia mais logo abaixo!!!\n")

print()

# Biografia de Bertha Lutz
nome = "bio_bertha_lutz.txt"
with open(nome, 'r', encoding='utf-8') as arq_entrada:
    conteudo = arq_entrada.read()

print(conteudo)
print()

