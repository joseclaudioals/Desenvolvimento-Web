import random

mega_sena = []
for _ in range(6):
    mega_sena.append(random.randint(1, 60+1))

acertos = 0
for i in range(6):
    n = int(input("Coloque o seu numero: "))
    acertos = acertos + 1 if n == mega_sena[i] else acertos

print(f"Quantidade de acertos: {acertos}")
print(f"Numeros premiados: {mega_sena}")