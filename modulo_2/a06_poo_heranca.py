# Crie uma classe chamada: Automóvel e crie classes filhas
class Automovel:
    def __init__(self, tipo, modelo, ano, km_rodados):
        self.tipo = tipo
        self.modelo = modelo
        self.ano = ano
        self.km_rodados = km_rodados


carro1 = Automovel("carro", "Tiggo", "2020", "100")
print(carro1.tipo)


# Classes filhas
class Carro(Automovel):
    def __init__(self, tipo, modelo, ano, km_rodados, qtd_portas):
        super().__init__(tipo, modelo, ano, km_rodados)
        self.qtd_portas = qtd_portas     # Diferencial da classse, pois uma moto, por exemplo, é um automóvel e não tem porta


    def especificacoes(self): 
        print(f"""O automóvel é do tipo {self.tipo}, 
              o modelo é {self.modelo}, 
              do ano {self.ano}, tem {self.qtd_portas} 
              portas e {self.km_rodados} Km rodados.\n""")


carroNovo = Carro("carro", "Tiggo", 2020, 150, 4)
carroNovo.especificacoes()


class Moto(Automovel):
    def __init__(self, tipo, modelo, ano, km_rodados, cilindradas):
        super().__init__(tipo, modelo, ano, km_rodados)
        self.cilindradas = cilindradas     # Diferencial da classe


    def especificacoes(self): 
        print(f"""O automóvel é do tipo {self.tipo}, 
              o modelo é {self.modelo}, 
              do ano {self.ano}, tem {self.cilindradas} 
              cilindradas e {self.km_rodados} Km rodados.\n""")


motoNova = Moto("moto", "Honda CB 500X", 2020, 40, 471)
motoNova.especificacoes()

