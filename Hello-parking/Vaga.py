from Veiculo import Veiculo


class Vaga:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.livre = True
        self.placa = None

    def ocupar(self, veiculo: Veiculo):
        self.livre = False
        self.placa = veiculo.placa

    def liberar(self):
        self.livre = True
        self.placa = None