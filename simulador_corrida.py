from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, modelo):
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        pass


class Carro(Veiculo):
    def acelerar(self):
        print(f"{self.modelo}: VAI, VAI, VAI! ")


class Moto(Veiculo):
    def acelerar(self):
        print(f"{self.modelo}: CORRE QUE A POLÍCIA VEM AÍ! ")


class Caminhao(Veiculo):
    def acelerar(self):
        print(f"{self.modelo}: SEGURA QUE O BICHÃO TÁ INDO! ")


class CarroEletrico(Veiculo):
    def acelerar(self):
        print(f"{self.modelo}: *modo silencioso ativado* ")


class UnoComEscada(Veiculo):
    def acelerar(self):
        print(f"{self.modelo}: 200 km/h NA DESCIDA! ")


class CeltaRebaixado(Veiculo):
    def acelerar(self):
        print(f"{self.modelo}: RASPANDO NO CHÃO, MAS TÁ ANDANDO! ")


class Fusca(Veiculo):
    def acelerar(self):
        print(f"{self.modelo}: DEMOROU 5 MINUTOS, MAS CHEGOU! ")


pista_de_corrida = [
    Carro("Gol Quadrado"),
    Moto("CG 160"),
    Caminhao("Caminhão Boiadeiro"),
    CarroEletrico("Tesla"),
    UnoComEscada("Uno com Escada"),
    CeltaRebaixado("Celta Rebaixado"),
    Fusca("Fusca do Lula")
]


for veiculo in pista_de_corrida:
    veiculo.acelerar()

