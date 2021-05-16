# ATIVIDADE: NO ESCURINHO DO CINEMA
print("_-"*41)
print("_-"*15, " Bem-vindo ao Clube!", "_-"*15)
print("_-"*41)

nome = input("Informe o seu nome: \n")
estuda_py = input("Você é estudante de Python? [S/N]\n")
idade = int(input("Qual a sua idade? \n"))

entrada_padrao = 35
entrada_vip = 60
idade_permitida = (18 - int(idade))

if idade >= 18 and estuda_py == "S":
    print("Escolha seu ingresso: \n Entrada padrão: R$ 35 \n Entrada VIP: R$ 60")
    input("Digite 1 ou 2: ")
    print("Bem-vindo ao Clube! Seu ingresso será 50% mais barato!")
else:
    if not idade < 18 and estuda_py == "S":
        print("Escolha seu ingresso: \n Entrada padrão: R$ 35 \n Entrada VIP: R$ 60")
        input("Digite 1 ou 2: ")
        print("Bem-vindo ao Clube! Seu ingresso será 50% mais barato!")
    elif idade < 18:
        print(f"Ainda faltam {idade_permitida} anos para você poder participar do clube!")

print()







