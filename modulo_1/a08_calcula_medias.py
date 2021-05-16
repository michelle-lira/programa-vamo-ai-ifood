# Você deverá utilizar o enunciado abaixo como base para desenvolver algoritmos 
# que utilizem todos os conceitos abordados no exercício anterior.  
# Uma professora deseja desenvolver um sistema para automatizar seu trabalho. 
# Ela precisa criar uma solução onde seus alunosconsigam inserir suas notas 
# (seja a média geral de todas asmatérias ou a média de uma única disciplina), 
# receber a média, esaber sua situação (aprovação, reprovação ou recuperação).
# Regras:Você pode misturar os conceitos abordados num mesmo programa;
# Você pode construir até 3 programas diferentes para conseguir abordar todos os conceitos;

# PARTE 1: MÉDIA DE 5 ALUNOS DIFERENTES EM UMA SÓ DISCIPLINA
def media_aluno(nota1, nota2, nota3, nota4):
    media = float(nota1 + nota2 + nota3 + nota4) / 4
    print(f"A sua média foi: {media}")

    if media >= 7.0:
        print("Você está aprovado! Parabéns!\n")
        if media > 9.0:
            print("Você está aprovado e com nota máxima! Parabéns!\n")
    elif media < 7.0 and media > 6.0:
        print("Você está de recuperação. Ainda não está aprovado.\n")
    else:
        print("Você está reprovado. Ainda não foi desta vez, mas tente novamente.\n")

aluno1_biologia = (8.0, 7.5, 10.0, 7.4)
media_aluno(8.0, 7.5, 10.0, 7.4)

aluno2_biologia = (10.0, 10.0, 10.0, 10.0)
media_aluno(10.0, 10.0, 10.0, 10.0)

aluno3_biologia = (4.0, 3.3, 6.7, 7.5)
media_aluno(8.0, 8.3, 6.7, 7.5)

aluno4_biologia = (7.0, 10.0, 10.0, 8.6)
media_aluno(7.0, 10.0, 10.0, 8.6)

aluno5_biologia = (4.4, 3.8, 3.4, 6.0)
media_aluno(4.4, 3.8, 3.4, 6.0)



# PARTE 2: MÉDIA DE 2 ALUNOS EM TODAS AS DISCIPLINAS
def media_aluno(nota1, nota2, nota3, nota4, nota5):
    media = float(nota1 + nota2 + nota3 + nota4 + nota5) / 5
    print(f"A sua média geral foi: {media}")

    if media >= 7.0:
        print("Você obteve um ótimo desempenho! Parabéns!\n")
        if media > 9.0:
            print("Você conseguiu a média máxima! Parabéns!\n")
    elif media < 7.0 and media > 6.0:
        print("O seu desempenho precisa melhorar.\n")
    else:
        print("O seu desempenho foi baixo. Converse com os seus professores e acompanhamento pedagógico.\n")

aluno1_portugues = 9.0
aluno1_matematica = 7.5
aluno1_biologia = 10.0
aluno1_fisica = 6.4
aluno1_quimica = 8.0
media_aluno(9.0, 7.5, 10.0, 6.4, 8.0)

aluno2_portugues = 10.0
aluno2_matematica = 8.0
aluno2_biologia = 3.0
aluno2_fisica = 7.0
aluno2_quimica = 7.5
media_aluno(10.0, 8.0, 3.0, 7.0, 7.5)



# PARTE 3: MÉDIA GERAL DA TURMA
def media_geral_turma(lista_media_alunos):
    lista_media_alunos = [8.0, 5.8, 9.5, 10.0, 7.3, 5.3, 4.0, 6.8, 6.2, 3.9, 10.0, 8.0, 7.2, 5.0, 9.9]
    media_geral = sum(lista_media_alunos) / len(lista_media_alunos)
    print(f"A média da turma é: {(media_geral):.2f}.")

    if media_geral >= 7.0:
        print("A turma teve um ótimo desempenho! Parabéns!\n")
    elif media_geral > 9.0:
        print("A turma alcançou desempenho máximo! Parabéns!\n")
    else:
        print("A média geral da turma precisa melhorar.\n")

media_aluno1 = 8.0
media_aluno2 = 5.8
media_aluno3 = 9.5
media_aluno4 = 10.0
media_aluno5 = 7.3
media_aluno6 = 5.3
media_aluno7 = 4.0
media_aluno8 = 6.8
media_aluno9 = 6.2
media_aluno10 = 3.9
media_aluno11 = 10.0
media_aluno12 = 8.0
media_aluno13 = 7.2
media_aluno14 = 5.0
media_aluno15 = 9.9

lista_media_alunos = [8.0, 5.8, 9.5, 10.0, 7.3, 5.3, 4.0, 6.8, 6.2, 3.9, 10.0, 8.0, 7.2, 5.0, 9.9]
media_geral_turma(lista_media_alunos)

