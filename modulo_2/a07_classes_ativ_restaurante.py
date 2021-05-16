# CLASSES -> Continuação da atividade do Restaurante:
class Pessoa:
    def __init__(self, nome, cpf, telefone, rg):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.rg = rg

    
    def comer(self, local, tipo_refeicao):
        self.local = local
        self.tipo_refeicao = tipo_refeicao


    def trabalhar(self, local, ocupacao):
        self.local = local
        self.ocupacao = ocupacao


class Entregador(Pessoa):
    def __init__(self, nome, cpf, telefone, rg, matricula, remuneracao):
        super().__init__(nome, cpf, telefone, rg)
        self.matricula = matricula
        self.remuneracao = remuneracao


    def comer(self, local, tipo_refeicao):
        self.local = local
        self.tipo_refeicao = tipo_refeicao


    def trabalhar(self, local, ocupacao):
        self.local = local
        self.ocupacao = ocupacao


class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, rg, endereco, pedido):
        super().__init__(nome, cpf, telefone, rg)
        self.endereco = endereco
        self.pedido = pedido


      def comer(self, local, tipo_refeicao):
        self.local = local
        self.tipo_refeicao = tipo_refeicao


    def trabalhar(self, local, ocupacao):
        self.local = local
        self.ocupacao = ocupacao


class Proprietario(Pessoa):
    def __init__(self, nome, cpf, telefone, rg, pro_labore, senha_desconto):
        super().__init__(nome, cpf, telefone, rg)
        self.pro_labore = pro_labore
        self.senha_desconto = senha_desconto

    
     def comer(self, local, tipo_refeicao):
        self.local = local
        self.tipo_refeicao = tipo_refeicao


    def trabalhar(self, local, ocupacao):
        self.local = local
        self.ocupacao = ocupacao
