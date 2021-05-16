#Crie um algoritmo que multiplique dois valores aleatórios entre 1 e 50. 
#Você deverá usarcondicionais e funções nesse processo.

import random

numero_aleatorio_1 = random.randrange(1,51)
numero_aleatorio_2 = random.randrange(1,51)

def multiplicar_aleatorios(aleatorio1, aleatorio2):
    produto = int(aleatorio1 * aleatorio2)
    print(aleatorio1)
    print(aleatorio2)
    print(produto)

multiplicar_aleatorios(numero_aleatorio_1, numero_aleatorio_2)