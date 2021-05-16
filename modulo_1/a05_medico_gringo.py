# Atividade: "Médico gringo"

print("*" * 51)
print('*' * 10, 'SERÁ QUE VOCÊ ESTÁ COM FEBRE?', '*' * 10)
print("*" * 51)

nome = input("Como você se chama? \n")

temperatura = float(input(f"Qual a sua temperatura {nome}? \n"))
print(f"Sua temperatura é: {temperatura} °C \n")

if temperatura > 37:
    print(f"Sinto muito {nome}, você está com febre. Melhor tomar um antitérmico.")
else:
    print(f"Você não está com febre {nome}. Volte para casa.")
    print()
