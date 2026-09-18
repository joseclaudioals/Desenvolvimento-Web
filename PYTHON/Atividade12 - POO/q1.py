class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def falar(self):
        print(f"Meu nome é {self._nome} e tenho {self._idade} anos.")


pessoa = Pessoa("Armandinho", 18)
pessoa.falar()