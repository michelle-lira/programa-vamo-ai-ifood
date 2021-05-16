#Faça um programa que contenha uma função que calcule a média 
# de cinco alunos (as notas decada aluno deverão ser distintas)

def media_aluno(nota1, nota2, nota3, nota4):
    media = float(nota1 + nota2 + nota3 + nota4) / 4
    print(f"A sua média foi: {media}")

    if media >= 7.0:
        print("Você está aprovado! Parabéns!")
        if media > 9.0:
            print("Você está aprovado e com nota máxima! Parabéns!")
    elif media < 7.0 and media > 6.0:
        print("Você está de recuperação. Ainda não está aprovado.")
    else:
        print("Você está reprovado. Ainda não foi desta vez, mas tente novamente.")

aluno1_portugues = (9.0, 7.5, 10.0, 6.4)
media_aluno(9.0, 7.5, 10.0, 6.4)

aluno2_portugues = (10.0, 10.0, 10.0, 10.0)
media_aluno(10.0, 10.0, 10.0, 10.0)

aluno3_portugues = (4.0, 3.3, 6.7, 7.5)
media_aluno(8.0, 8.3, 6.7, 7.5)

aluno4_portugues = (7.0, 10.0, 10.0, 8.6)
media_aluno(7.0, 10.0, 10.0, 8.6)

aluno5_portugues = (4.4, 3.8, 3.4, 6.0)
media_aluno(4.4, 3.8, 3.4, 6.0)


    