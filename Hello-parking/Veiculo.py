class Veiculo:
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False

    def estacionar(self):
        self.estacionado = True

    def retirar(self):
        self.estacionado = False

