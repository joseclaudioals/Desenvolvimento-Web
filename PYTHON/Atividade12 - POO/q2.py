class Carro:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def ligar(self):
        print(f"Ligando o motor a combustao")

class Eletrico(Carro):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def ligar(self):
        print(f"Ligando o motor eletrico")


carro = Eletrico("Armandinho", 'barato')
carro.ligar()
