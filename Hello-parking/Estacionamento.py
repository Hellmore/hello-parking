from Vaga import Vaga
from Carro import Carro
from Moto import Moto

class Estacionamento:
    def __init__(self):
        self.qtd_vagas_motos = 25
        self.qtd_vagas_carros = 25
        self.vagas_para_motos = []
        self.vagas_para_carros = []

        for i in range(self.qtd_vagas_motos):
            self.vagas_para_motos.append(Vaga(f"M{i}", "moto"))

        for i in range(self.qtd_vagas_carros):
            self.vagas_para_carros.append(Vaga(f"C{i}", "carro"))

    def estacionar_carro(self, carro: Carro):
        for vaga in self.vagas_para_carros:
            if vaga.livre:
                vaga.ocupar(carro)
                carro.estacionar()
                break

        if carro.estacionado:
            print("Estacionado com sucesso")
        else:
            print("Estacionamento cheio")

    def estacionar_moto(self, moto: Moto):
        for vaga in self.vagas_para_motos:
            if vaga.livre:
                vaga.ocupar(moto)
                moto.estacionar()
                break

        if moto.estacionado:
            print("Estacionado com sucesso")
        else:
            for vaga in self.vagas_para_carros:
                if vaga.livre:
                    vaga.ocupar(moto)
                    moto.estacionar()

            if moto.estacionado:
                print("Estacionado com sucesso.")
            else:
                print("Estacionamento cheio.")

    def remover_carro(self, carro: Carro):
        for vaga in self.vagas_para_carros:
            if not vaga.livre and vaga.placa == carro.placa:
                vaga.liberar()
                carro.retirar()

        if not carro.estacionado:
            print("Removido com sucesso.")
        else:
            print("Este carro não esta estacionado neste estacionamento")

    def remover_moto(self, moto: Moto):
        for vaga in self.vagas_para_motos:
            if not vaga.livre and vaga.placa == moto.placa:
                vaga.liberar()
                moto.retirar()

        if not moto.estacionado:
            print("Removido com sucesso.")
        else:
            for vaga in self.vagas_para_carros:
                if not vaga.livre and vaga.placa == moto.placa:
                    vaga.liberar()
                    moto.retirar()

            if not moto.estacionado:
                print("Removido com sucesso.")
            else:
                print("Este carro não esta estacionado neste estacionamento")

    def vagas_disponiveis(self):
        vagas_carro = 0
        vagas_moto = 0

        for vaga in self.vagas_para_carros:
            if vaga.livre:
                vagas_carro += 1

        for vaga in self.vagas_para_motos:
            if vaga.livre:
                vagas_moto += 1

        print(f"Temos Vagas para: \n"
              f"{vagas_carro} Carros e {vagas_moto} Motos")


estacionamento = Estacionamento()

vectra = Carro("AAA00123")
moto1 = Moto("MOTOMA2312321")

estacionamento.estacionar_carro(vectra)
estacionamento.estacionar_moto(moto1)

estacionamento.vagas_disponiveis()

estacionamento.remover_carro(vectra)
estacionamento.remover_moto(moto1)

estacionamento.vagas_disponiveis()