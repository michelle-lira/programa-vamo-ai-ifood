#Faça uma função que calcule se o resultado do exame do paciente está "bom", "médio" ou"ruim". 
#O algoritmo deve conter, pelo menos, três pacientes (um em cada situação).Considere os parâmetros:      
#Bom = entre 7 e 10;      Médio = entre 4 e 6;      Ruim = entre 0 e 3;
#Dependendo do resultado, você deve aconselhá-lo a:      
#Bom = Continuar assim;        Médio = Buscar se cuidar mais e fazer acompanhamento médico;      Ruim = Procurar a equipe médica;

def resultado_exame(estado_geral_de_saúde):
    if estado_geral_de_saúde >= 7 and estado_geral_de_saúde <= 10:
        bom = "Continuar assim.\n"
        print(bom)
    elif estado_geral_de_saúde >= 4 and estado_geral_de_saúde <=6:
        medio = "Buscar se cuidar mais e fazer acompanhamento médico.\n"
        print(medio)
    elif estado_geral_de_saúde >= 0 and estado_geral_de_saúde <=3:
        ruim = "Procurar a equipe médica."
        print(ruim)
    else:
        print("Resultados inconclusivos. Refaça o exame.\n")

paciente1 = 30
resultado_exame(30)

paciente2 = 7
resultado_exame(7)


