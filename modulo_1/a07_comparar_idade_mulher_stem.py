#Faça um programa que calcule a diferença entre a sua idade e a 
#da mulher de STEM que vocêpesquisou na última aula. 
#Você também deve comparar o estado e país de vocês,
# e exibir isso na tela de uma maneira que fique claro para quem está lendo
# Funções e operadores de comparação deverão ser utilizados nesse processo.


ano_nascimento_usuario = int(input("Qual o ano em que você nasceu? \n"))
estado_usuário = input("Em qual Estado você nasceu? \n")
pais_usuário = input("Em qual país você nasceu? \n")

ano_nascimento_mulher_stem = 1894
estado_mulher_stem = "São Paulo"
pais_mulher_stem = "Brasil"

#Idade
def comparar_idade(ano_nascimento1, ano_nascimento2):
    resultado = int(abs(ano_nascimento1 - ano_nascimento2))
    print(resultado)

    if ano_nascimento1 < ano_nascimento2:
        print(f"Você é mais velho(a) que a mulher stem {resultado} anos!")
    elif ano_nascimento2 < ano_nascimento1:
        print(f"Você é mais novo(a) que a mulher stem {resultado} anos!")
    else:
        print(f"Você tem a mesma idade que a mulher stem! {resultado} anos!")

comparar_idade(ano_nascimento_usuario, ano_nascimento_mulher_stem)

#Estado
def comparar_estado(estado1, estado2):
    if estado1 == estado2:
        print("Vocês nasceram no mesmo estado.")
    else:
        print(f"Vocês nasceram em estados diferentes. Você nasceu em {estado1} e Bertha Lutz nasceu em {estado2}.")

comparar_estado(estado_usuário, estado_mulher_stem)

#País
def comparar_pais(nacao1, nacao2):
    if nacao1 == nacao2:
        print("Vocês nasceram no mesmo país.")
    else:
        print(f"Vocês nasceram em países diferentes. Bertha Lutz nasceu no: {nacao2}")

comparar_pais(pais_usuário, pais_mulher_stem)

