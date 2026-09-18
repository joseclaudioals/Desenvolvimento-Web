from q1 import Pessoa

lista = []
pai = Pessoa("Jorge", 40)
lista.append(pai)
mae = Pessoa("Maria", 38)
lista.append(mae)
filho = Pessoa("Enzo", 15)
lista.append(filho)
filha = Pessoa("Evelyn", 8)
lista.append(filha)

for p in lista:
    p.falar()
